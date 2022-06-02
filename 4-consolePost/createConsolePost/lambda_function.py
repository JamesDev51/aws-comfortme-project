import json
import sys
import logging
import pymysql
import boto3
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
        
        comprehend = boto3.client(service_name='comprehend', region_name='ap-northeast-2',aws_access_key_id='AKIAUI2WSCLQZYBOH6L7', aws_secret_access_key='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')
        retVal=comprehend.detect_sentiment(Text=contents, LanguageCode='ko')
        sentimentScore=retVal['SentimentScore']
        positive=sentimentScore['Positive']
        negative=sentimentScore['Negative']
        
        
        sql = "INSERT INTO ConsolePost(title,contents,email,anonymous,mainCategory,subCategory,positive,negative) VALUES(%(title)s,%(contents)s,%(email)s,%(anonymous)s,%(mainCategory)s,%(subCategory)s,%(positive)s,%(negative)s)"
        sqlData={
            'title':title,
            'contents':contents,
            'email':email,
            'anonymous':anonymous,
            'mainCategory':mainCategory,
            'subCategory':subCategory,
            'positive':positive,
            'negative':negative
        }
        conductSqlQuery(sql,sqlData)
        
        
        result={'statusCode':HTTPStatus.OK}
        print("createConsolePost lambda_handler function done")
        print("--------------------------------")
        return result
    except Exception:
        logging.exception(Exception)
