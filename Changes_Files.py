#!/usr/bin/env/python
import mysql.connector
from mysql.connector import errorcode
from Module1_Db_Connectivity import DB_NAME
cnx=mysql.connector.connect(user='ashish',password='9213747927',host='127.0.0.1',database=DB_NAME)

cursor=cnx.cursor()
query=("SELECT Previous_Reading FROM Meter_No1 Where NAME=input((first_name)And (Billing_Cycle-1)) ")
cursor.execute(query)
cursor.close()
cnx.close()

