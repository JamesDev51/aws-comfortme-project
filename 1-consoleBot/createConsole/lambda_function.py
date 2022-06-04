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
        print("createConsole lambda_handler function init")
        print("event : ",event)
        
        data=json.loads(event['body'])
        request=data['request']
        email=data['email']
        print(f"request : {request}   email : {email}")
        
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        retVal=requests.post('https://0mo7o614ha.execute-api.ap-northeast-2.amazonaws.com/dev/console-chatbot', headers=headers,timeout=60,json={'request':request})
        print("retVal : ",retVal.json())
        retVal=retVal.json()
        
        
        
        response=retVal['response']
        division=retVal['division']
        simRequest=retVal['simRequest']
        simRate=retVal['simRate'] 
        

        
        sql = "INSERT INTO ConsoleBot(request,response,email,division,simRequest,simRate) VALUES(%(request)s,%(response)s,%(email)s,%(division)s,%(simRequest)s,%(simRate)s)"
        sqlData={
            'request':request,
            'response':response,
            'email':email,
            'division':division,
            'simRequest':simRequest,
            'simRate':simRate
        }
        conductSqlQuery(sql,sqlData)
        
        retVal['request']=request
        retVal['email']=email
        
        
        result={
        'statusCode':HTTPStatus.OK,
        'headers': {
            'Access-Control-Allow-Origin': '*',
        },
        'body':json.dumps(retVal),
        }
        
        print("createConsole lambda_handler function done")
        print("--------------------------------")
        return result
    except Exception:
        logging.exception(Exception)
