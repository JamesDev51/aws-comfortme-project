import json
import sys
import logging
import pymysql
from http import HTTPStatus
import requests

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
        # data=json.loads(event['body'])
        data=event['body']
        
        request=data['request']
        email=data['email']
        print(f"request : {request}   email : {email}")
        
        '''
        TODO : chatbot으로부터 받아오는 부분 fixing 필요 
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        response=requests.post('https://opgftpltze.execute-api.ap-northeast-2.amazonaws.com/default/console_chatbot', headers=headers,timeout=40,json={'request':request})
        print("response : ",response.json())
        '''
        
        response="수고하셨어요" #임시 response
        division=1 #임시 div
        simRequest="남편이 저에게 안좋게 말해요" #임시 simRequest
        simRate=0.98384 #임시 simRate
        print(f"response : {response}   division : {division}   simRequest : {simRequest}   simRate : {simRate}")
    

        
        sql = "INSERT INTO console(request,response,email,division,simRequest,simRate) VALUES(%(request)s,%(response)s,%(email)s,%(division)s,%(simRequest)s,%(simRate)s)"
        sqlData={
            'request':request,
            'response':response,
            'email':email,
            'division':division,
            'simRequest':simRequest,
            'simRate':simRate
        }
        conductSqlQuery(sql,sqlData)
        
        result={'status':HTTPStatus.OK}
        print("createConsole lambda_handler function done")
        print("--------------------------------")
        return result
    except Exception:
        logging.exception(Exception)
