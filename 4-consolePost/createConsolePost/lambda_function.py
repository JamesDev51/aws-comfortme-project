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
        print("createConsolePost lambda_handler function init")
        print("event : ",event)
        
        title=event['title']
        contents=event['contents']
        email=event['email']
        anonymous=event['anonymous']
        mainCategory=event['mainCategory']
        subCategory=event['subCategory']
        print(f"title : {title}   contents : {contents}   anonymous : {anonymous}   mainCategory : {mainCategory}   subCategory : {subCategory}")
        
        sql = "INSERT INTO ConsolePost(title,contents,email,anonymous,mainCategory,subCategory) VALUES(%(title)s,%(contents)s,%(email)s,%(anonymous)s,%(mainCategory)s,%(subCategory)s)"
        sqlData={
            'title':title,
            'contents':contents,
            'email':email,
            'anonymous':anonymous,
            'mainCategory':mainCategory,
            'subCategory':subCategory
        }
        conductSqlQuery(sql,sqlData)
        
        
        result={'statusCode':HTTPStatus.OK}
        print("createConsolePost lambda_handler function done")
        print("--------------------------------")
        return result
    except Exception:
        logging.exception(Exception)
