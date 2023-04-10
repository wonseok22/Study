import math
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



# def divide_by_sum_of_nutrient():
#     """
#     Desc :
#         영양소의 가중치를 구할 때, (음식 별 영양소 함유량)/(모든 음식의 영양소 총합)로 구한 결괏값을 반환하는 함수.
#
#     Args :
#         data : 정규화 할 데이터, 모든 column은 영양소이며 0행은 각 영양소의 명칭이다.
#
#     Returns :
#         Datafreme 형태로 모든 음식의 각 영양소를 0-1 정규화하여 반환
#     """
#     df = pd.read_excel('C:/Users/SSAFY/Downloads/영양.xlsx')
#     # 수정 필요

#
#
#     for row in range(len(df.index)):
#         name = df['식품명'][row]
#         description = df['설명'][row]
#         time = df['조리시간'][row]
#         efficiency = df['효능'][row]
#         amount = df['1회제공량'][row]
#         unit = df['내용량'][row]
#         # query = "INSERT INTO pnut.food (name, description, time, efficiency, amount, unit) VALUES('"+name+"','"+description+"',"+str(time)+",'"+efficiency +"'," + str(amount) + ",'" + unit + "')"
#         # cursor.execute(query)
#         # conn.commit()
#
#         query = "SELECT * FROM food where name ='" + name + "'; " # 중복체크
#         cursor.execute(query)
#         r = cursor.fetchone()
#         print("인덱스 = ", r[0])
#
#

# def regist_recommned_nutrient():
#     gender = ["남성","여성"]
#     for i in range(1,25):
#         query = "SELECT * FROM nutrient_rec where nutrient_id ='" + str(i) + "'; "
#         cursor.execute(query)
#         result = cursor.fetchone()
#         if result:
#             print("이미 있는 영양소입니다.")
#             continue
#         query = "SELECT name,unit FROM nutrient where nutrient_id ='" + str(i) + "'; "  # 중복체크
#         cursor.execute(query)
#         result = cursor.fetchone()
#
#         print(result)
#         print("있는 영양소인가요? 없으면 pass 입력")
#         check = input()
#         if check == "pass":
#             continue
#         for j in range(1,8):
#             print(j*10,"세 부터",j*10+9,"까지 영양소 입력")
#             for k in range(2):
#                 print(gender[k],"의 영양소 입력")
#                 print("단위를 맞추세요")
#                 g = str(k)
#                 a = str(j)
#                 n = str(i)
#                 w = input()
#                 query = "INSERT INTO nutrient_rec(gender,age,nutrient_id,weight) VALUES(" + g + "," + a + "," + n + "," + w + ");"
#                 cursor.execute(query)
#         conn.commit()
#         print(result,"저장되었습니다.")
#     conn.close()
# def regist_food():
#     df = pd.read_excel('C:/Users/SSAFY/Downloads/영양소 최종본 입력용.xlsx')
#     sum_of_nutrient = [0 for _ in range(24)]
#     for index in range(1, 24):
#         sum_of_nutrient[index] = df[index].sum()
#     for row in range(len(df.index)):
#         name = df['식품명'][row]
#         description = df['설명'][row]
#         time = df['조리시간'][row]
#         efficiency = df['효능'][row]
#         amount = df['1회제공량'][row]
#         unit = df['내용량_단위'][row]
#         ing = df["재료"][row]
#         cat = df["카테고리"][row]
#         cat = str(cat)
#         cat = cat.split(",")
#         print(name)
#         if pd.isna(ing):
#             print("재료 비어있음!!@", name)
#             continue
#         ingredients = df["재료"][row].split(",")
#         url = df["url"][row]
#         query = "SELECT * FROM food where name ='" + name + "'; " # 중복체크
#         cursor.execute(query)
#         r = cursor.fetchone()
#         if r:
#             print("이미 있는 음식입니다.", name)
#             continue
#         if pd.isna(description) or pd.isna(efficiency)  or pd.isna(url) or pd.isna(time):
#             print("완성되지 않은 음식" , name)
#             continue
#         query = "INSERT INTO pnut.food (name, description, time, efficiency, amount, unit, ingredients, url) VALUES('"+name+"','"+description+"',"+str(time)+",'"+efficiency +"'," + str(amount) + ",'" + unit + "','" + ing + "','" + url +"');"
#         cursor.execute(query)
#         conn.commit()
#         query = "SELECT * FROM food where name ='" + name + "'; " #몇 번 요리인지 확인
#         cursor.execute(query)
#         r = cursor.fetchone()
#         food_id = r[0]
#         print(food_id, "food_id는?")
#         print("인덱스 = ", r[0])
#         for i in cat:
#             query = 'INSERT INTO pnut.food_cat(food_id, cat_id) VALUES(' + str(food_id) + ','+ str(i) + ');'
#             cursor.execute(query)
#             conn.commit()
#         for i in ingredients:
#             index = 0
#             query = "SELECT * FROM pnut.ingredient WHERE name ='" + i + "';"
#             cursor.execute(query)
#             r = cursor.fetchone()
#             if r:
#                 index = r[0]
#             else:
#                 query = "INSERT INTO pnut.ingredient (name) VALUES('"+ i +"');"
#                 cursor.execute(query)
#                 conn.commit()
#                 query = "SELECT * FROM pnut.ingredient WHERE name ='" + i + "';"
#                 cursor.execute(query)
#                 r = cursor.fetchone()
#                 index=r[0]
#             query = "INSERT INTO pnut.food_ingre (ingredient_id, food_id) VALUES(" + str(index) + "," + str(food_id) + ");"
#             cursor.execute(query)
#         conn.commit()
#         for index in range(1, 24):
#             if df[index][row] == '-' or df[index][row] == 0: continue
#             nutrient = float(df[index][row])
#             nutrient_percent = nutrient/sum_of_nutrient[index]
#             query = "INSERT INTO pnut.food_nut (nutrient_id, food_id, weight, weight_percent) VALUES(" + str(index) + "," + str(food_id) + "," + str(nutrient) + "," + str(nutrient_percent) +")"
#             cursor.execute(query)
#         conn.commit()

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


query = "SELECT * FROM pnut.food_nut WHERE nutrient_id=1"
cursor.execute(query)
for c in cursor.fetchall():
    query = "UPDATE pnut.food SET cal =" + str(c[3]) + " WHERE food_id = " + str(c[2]) + ";"
    cursor.execute(query)
    conn.commit()
conn.commit()


