import sys
import os
import pymysql
import base64
import requests
import pandas as pd
import openpyxl
host = "pnut.cr7lqn4qteql.ap-northeast-2.rds.amazonaws.com"
port = 3306
username = "admin"
database = "pnut"
password = "asdf1234"


def connect(host, port, username, password, database):
    try :
        conn = pymysql.connect(
            host="pnut.cr7lqn4qteql.ap-northeast-2.rds.amazonaws.com",
            port=3306,
            user="admin",
            password="asdf1234",
            database="pnut"
        )
        cursor = conn.cursor()
    except:
        exit(-1)
    return conn,cursor


conn, cursor = connect(host,port,username,password,database)

r = pd.read_excel('C:/Users/SSAFY/Downloads/영양.xlsx',sheet_name = 0,header = 1)
for i in r.values:
    if i[4] == "품목대표":
        print(i)



# query = "SELECT * FROM user"
# cursor.execute(query)
# result = cursor.fetchall()
# for r in result:
#     print(r)
conn.commit()