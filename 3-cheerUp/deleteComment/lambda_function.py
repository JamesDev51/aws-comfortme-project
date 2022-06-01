import json
import sys
import logging
import pymysql
import datetime
from http import HTTPStatus

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
        print("deleteComment lambda_handler function init")
        
        params=event['queryStringParameters']
        commentId=params["commentId"]
        
        sql = "DELETE FROM Comment WHERE commentId=%s"
        conductSqlQuery(sql, commentId)
        
        result={"statusCode":HTTPStatus.OK}
        print("deleteComment lambda_handler function done")
        print("--------------------------------")
        return result
    except Exception:
        logging.exception(Exception)