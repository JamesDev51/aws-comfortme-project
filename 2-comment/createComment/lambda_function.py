import json
import sys
import logging
import pymysql
from http import HTTPStatus
import requests

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

def  conductSqlQuery(sql, sqlData):
    print("--------------------------------")
    print("conductSqlQuery function init")
    conn=getMysqlConn()
    curs = conn.cursor()
    curs.execute(sql, sqlData) 
    conn.commit()
    print("conductSqlQuery function done")
    print("--------------------------------")

def lambda_handler(event, context):
    try:
        print("--------------------------------")
        print("createComment lambda_handler function init")
        contents=event['contents']
        consolePostId=event['consolePostId']
        email=event['email']
        anonymous=event['anonymous']
        print(f"contents : {contents}  consolePostId : {consolePostId}   email : {email}  anonymous : {anonymous}")
        
        
        sql = "INSERT INTO Comment(contents,consolePostId,email,anonymous) VALUES(%(contents)s,%(consolePostId)s,%(email)s,%(anonymous)s)"
        sqlData={
            'contents':contents,
            'consolePostId':consolePostId,
            'email':email,
            'anonymous':anonymous
        }
        conductSqlQuery(sql,sqlData)
        
        result={'statusCode':HTTPStatus.OK}
        print("createComment lambda_handler function done")
        print("--------------------------------")
        return result
    except Exception:
        logging.exception(Exception)
