import json
import sys
import logging
import pymysql
from http import HTTPStatus
import numpy as np

DB_HOST="db-team8-consolation.c8fut6pj2ay8.ap-northeast-2.rds.amazonaws.com"
DB_USER="root"
DB_PASSWORD="1tkddydwkdql"
DB_NAME="comfortmeDB"



def getMysqlConn():
    return pymysql.connect(
            host=DB_HOST, 
            user=DB_USER, 
            password=DB_PASSWORD, 
            db=DB_NAME)

def  conductSqlQuery(sql,sqlData):
    print("--------------------------------")
    print("conductSqlQuery function init")
    conn=getMysqlConn()
    curs = conn.cursor()
    with conn:
        with conn.cursor(pymysql.cursors.DictCursor) as cur:
                cur.execute(sql,sqlData)
                # result = json.dumps(cur.fetchall(),default=json_default,ensure_ascii = False)
                result = cur.fetchall()
    print("conductSqlQuery function done")
    print("--------------------------------")
    return result

def  conductSqlQuery2(sql, sqlData):
    print("--------------------------------")
    print("conductSqlQuery2 function init")
    conn=getMysqlConn()
    curs = conn.cursor()
    curs.execute(sql, sqlData)
    conn.commit()
    print("conductSqlQuery2 function done")
    print("--------------------------------")
    

def lambda_handler(event, context):
    try:
        print("--------------------------------")
        print("createConsolePost lambda_handler function init")
        print("event : ",event)
        data=json.loads(event['body'])
    
        email=data['email']
        consolePostId=data['consolePostId']
        
        print("email : ",email  ,"  consolePostId : ",consolePostId )
        
        sql = "SELECT * FROM ConsolePost WHERE consolePostId=%s"
        consolePost=conductSqlQuery(sql,consolePostId)
        consolePost=consolePost[0]
        
        sql="SELECT * FROM UserEmbedding WHERE email=%s"
        user=conductSqlQuery(sql,email)
        user=user[0]
        print("user : ",user)

        result={'statusCode':HTTPStatus.OK,'headers': {
                'Access-Control-Allow-Origin': '*',
            }
        }
        
        if len(user)==0:
            bertEmbedding=consolePost['bertEmbedding']
            sql="INSERT INTO UserEmbedding(email,bertEmbedding) VALUES (%(email)s, %(bertEmbedding)s)"
            sqlData={
                'email':email,
                'bertEmbedding':bertEmbedding}
            conductSqlQuery2(sql,sqlData)
            return result
        else:
            bertEmbedding=np.fromstring(consolePost['bertEmbedding'].replace('[','').replace(']',''),sep=', ')
            userBertEmbedding=np.fromstring(user['bertEmbedding'].replace('[','').replace(']',''),sep=', ')
            newUserBertEmbedding=bertEmbedding+userBertEmbedding
            newUserBertEmbedding = str(newUserBertEmbedding.tolist())
            
            sql = "UPDATE UserEmbedding SET bertEmbedding=%(bertEmbedding)s WHERE email=%(email)s"
            sqlData={
                'email':email,
                'bertEmbedding':newUserBertEmbedding
            }
            conductSqlQuery2(sql,sqlData)
            return result
        
        print("createConsolePost lambda_handler function done")
        print("--------------------------------")
        return result
    except Exception:
        logging.exception(Exception)
