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
nutrients = [
    "열량",
    "단백질",
    "지방",
    "탄수화물",
    "포도당",
    "식이섬유",
    "칼슘",
    "철",
    "마그네슘",
    "인",
    "칼륨",
    "나트륨",
    "아연",
    "구리",
    "망간",
    "베타카로틴",
    "비타민D",
    "비타민B",
    "엽산",
    "비타민C",
    "콜레스테롤",
    "포화지방산",
    "트랜스지방산",
    "오메가3"
]
unit = [
    "kcal",
    "g",
    "g",
    "g",
    "g",
    "g",
    "g",
    "mg",
    "mg",
    "mg",
    "mg",
    "mg",
    "mg",
    "mg",
    "mg",
    "mg",
    "µg",
    "µg",
    "mg",
    "µg",
    "mg",
    "mg",
    "g",
    "g",
    "µg"
]
category = [
    "마음",
    "피부",
    "구강관리",
    "다이어트",
    "뼈/관절",
    "피로/활력",
    "간 건강",
    "장 건강",
    "모발/두피",
    "위/소화",
    "면역력"
]

while True:
    print("질문 번호 입력")
    question_num = input()
    if question_num == -1:
        print("정상적으로 종료되었씁니다.")
        break
    print("영양소 번호 입력")
    nut_num = input()
    query = "INSERT INTO pnut.nut_quest (question_id, nutrient_id) VALUES('" + question_num + "',"+ nut_num + ");"
    cursor.execute(query)
    conn.commit()

# while True:
#     print("설문 내용 입력")
#     content = input()
#     if content == "exit":
#         break
#     print("카테고리 번호 입력")
#     category_num = input()
#     query = "INSERT INTO pnut.question (content, category_id) VALUES('" + content + "',"+ category_num + ");"
#     cursor.execute(query)
#     conn.commit()


# for category_name in category:
#     query = "SELECT * FROM pnut.category where category_name ='" + category_name + "'; "
#     cursor.execute(query)
#     if cursor.fetchall():
#         print("이미 있는 영양소입니다.")
#         continue
#     query = "INSERT INTO pnut.category (category_name) VALUES('" + category_name + "');"
#     cursor.execute(query)
#     conn.commit()

# for i in range(len(nutrients)):
#     nut_name = nutrients[i]
#     nut_unit = unit[i]
#     query = "SELECT * FROM pnut.nutrient where name ='" + nut_name + "'; "
#     cursor.execute(query)
#     if cursor.fetchall():
#         print("이미 있는 영양소입니다.")
#         continue
#     print(nut_name)
#     print("가이드를 입력하세요")
#     guide = input()
#     print("설명을 입력하세요")
#     desc = input()
#     print("태그 1을 입력하세요")
#     tag1 = input()
#     print("태그 2를 입력하세요")
#     tag2 = input()
#     query = "INSERT INTO pnut.nutrient (name, guide, description, tag1, tag2, unit) VALUES('" + nut_name + "','" + guide + "','" + desc + "','" + tag1 + "','" + tag2 + "','" + nut_unit + "');"
#     cursor.execute(query)
#     conn.commit()

# r = pd.read_excel('C:/Users/SSAFY/Downloads/영양.xlsx',sheet_name = 0,header = 1)
# for row in r.values:
#     print(i[5] + "차례")
#     ing = list()
#     name = i[2]
#     query = "SELECT * FROM food where name ='" + name + "'; " # 중복체크
#     cursor.execute(query)
#
#     if cursor.fetchall():
#         print("이미 있는 음식입니다.")
#         continue
#
#     while True: # 해당 음식의 재료 입력 받기
#         data = input()
#         if data == "exit":
#             break
#         ing.append(data)
#
#     print("설명 입력")
#     desc = input()
#     print("효능 입력")
#     eff = input()
#     print("조리시간 입력")
#     time = int(input())
#     for i in ing:
#         query = "SELECT * FROM "
#     query = ""
#     query = "INSERT INTO pnut.food (name, description, time, efficiency) VALUES('"+name+"','"+desc+"',"+str(time)+",'"+eff+"')"
#     cursor.execute(query)
#     conn.commit()


# query = "SELECT * FROM user"
# cursor.execute(query)
# result = cursor.fetchall()
# for r in result:
#     print(r)
