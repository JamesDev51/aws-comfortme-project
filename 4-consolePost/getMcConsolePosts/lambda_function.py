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

def  conductSqlQuery(sql,sqlData):
    print("--------------------------------")
    print("conductSqlQuery function init")
    conn=getMysqlConn()
    curs = conn.cursor()
    with conn:
        with conn.cursor(pymysql.cursors.DictCursor) as cur:
                cur.execute(sql,sqlData)
                result = json.dumps(cur.fetchall(),default=json_default,ensure_ascii = False)
    print("conductSqlQuery function done")
    print("--------------------------------")
    return result

def json_default(value): 
    if isinstance(value, datetime.date): 
        return value.strftime('%Y-%m-%d %H:%M:%S') 
    raise TypeError('not JSON serializable')

def lambda_handler(event, context):
    try:
        print("--------------------------------")
        print("getMcConsolePosts lambda_handler function init")
        print("event : ",event)
        params=event['queryStringParameters']

        category=params['mainCategory']
        page=params['page']
        print("mainCategory : ",category, "page : ",page)
        
        mainCategory,subCategory=category.split("/")
        mainCategory=f"%{mainCategory}%"
        subCategory=f"%{subCategory}%"
        
        limit=str((int(page)+1)*10-1)
        offset=str(int(page)*10)
        
        
        # sql = f"SELECT * FROM ConsolePost WHERE (mainCategory LIKE %(mainCategory)s  OR subCategory LIKE %(subCategory)s) ORDER BY createdAt DESC LIMIT {limit} OFFSET {offset}"
        sql = f"select cp.*, (select count(*) from Comment c where c.consolePostId=cp.consolePostId) as commentCount,(select count(*) from CheerUp ch where ch.consolePostId=cp.consolePostId) as cheerUpCount from ConsolePost cp WHERE (cp.mainCategory LIKE %(mainCategory)s  OR cp.subCategory LIKE %(subCategory)s) ORDER BY cp.createdAt DESC LIMIT {limit} OFFSET {offset}"
        sqlData={
            'mainCategory':mainCategory,
            'subCategory':subCategory
        }
        retValue=conductSqlQuery(sql,sqlData)
        
        result={
            'statusCode':HTTPStatus.OK,
            'headers': {
                'Access-Control-Allow-Origin': '*',
            },
            'body':retValue
        }
        print("getMcConsolePosts lambda_handler function done")
        print("--------------------------------")
        return result
    except Exception:
        logging.exception(Exception)