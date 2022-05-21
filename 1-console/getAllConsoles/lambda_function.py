import json
import sys
import logging
import pymysql
import datetime
from http import HTTPStatus

DB_HOST="db-team8-consolation.c8fut6pj2ay8.ap-northeast-2.rds.amazonaws.com"
DB_USER="root"
DB_PASSWORD="1tkddydwkdql"
DB_NAME="helpmeDB"

def getMysqlConn():
    return pymysql.connect(
            host=DB_HOST, 
            user=DB_USER, 
            password=DB_PASSWORD, 
            db=DB_NAME)

def  conductSqlQuery(sql):
    print("--------------------------------")
    print("conductSqlQuery function init")
    conn=getMysqlConn()
    curs = conn.cursor()
    with conn:
        with conn.cursor(pymysql.cursors.DictCursor) as cur:
                cur.execute(sql)
                result = json.dumps(cur.fetchall(),default=json_default,ensure_ascii = False)
    print("conductSqlQuery function done")
    print("--------------------------------")
    return result

def json_default(value): 
    if isinstance(value, datetime.date): 
        return value.strftime('%Y-%m-%d') 
    raise TypeError('not JSON serializable')

def lambda_handler(event, context):
    try:
        print("--------------------------------")
        print("getAllConsoles lambda_handler function init")

        conn=getMysqlConn()
        sql = "SELECT * FROM console"
        retValue=conductSqlQuery(sql)
        
        result={
            'statusCode':HTTPStatus.OK,
            'body':retValue
        }
        print("getAllConsoles lambda_handler function done")
        print("--------------------------------")
        return result
    except Exception:
        logging.exception(Exception)