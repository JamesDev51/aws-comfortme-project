import json
import sys
import logging
import pymysql
from http import HTTPStatus
import requests
import datetime

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
    
def  conductSqlQuery1(sql,sqlData):
    print("--------------------------------")
    print("conductSqlQuery1 function init")
    conn=getMysqlConn()
    curs = conn.cursor()
    with conn:
        with conn.cursor(pymysql.cursors.DictCursor) as cur:
                cur.execute(sql,sqlData)
                result = json.dumps(cur.fetchall(),default=json_default,ensure_ascii = False)
    print("conductSqlQuery1 function done")
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

def json_default(value): 
    if isinstance(value, datetime.date): 
        return value.strftime('%Y-%m-%d %H:%M:%S') 
    raise TypeError('not JSON serializable')



def lambda_handler(event, context):
    try:
        print("--------------------------------")
        print("createCheerUp lambda_handler function init")
        data=json.loads(event['body'])
        
        
        consolePostId=data['consolePostId']
        email=data['email']
        print(f"consolePostId : {consolePostId}   email : {email}")

        sqlData={
            'consolePostId':consolePostId,
            'email':email
        }
        
        sql = "SELECT * FROM CheerUp WHERE consolePostId= %(consolePostId)s AND email=%(email)s"
        retValue=conductSqlQuery1(sql,sqlData)
        print("retValue : ", retValue)
        if str(retValue)!="[]":
            result={'statusCode':HTTPStatus.BAD_REQUEST, 'body':"이미 힘내요를 누르셨습니다."}
            return result
        
        
        sql = "INSERT INTO CheerUp(consolePostId,email) VALUES(%(consolePostId)s,%(email)s)"
        conductSqlQuery2(sql,sqlData)
        
        result={'statusCode':HTTPStatus.OK}
        print("createCheerUp lambda_handler function done")
        print("--------------------------------")
        return result
    except Exception:
        logging.exception(Exception)
