#!/usr/bin/env/python
from __future__ import print_function
import mysql.connector
from mysql.connector import errorcode
from Module1_Db_Connectivity import DB_NAME
try:
    cnx=mysql.connector.connect(user='ashish',password='9213747927',host='127.0.0.1',database=DB_NAME)
except mysql.connector.Error as err:
    if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
        print('Something is wrong with the name')
    elif err.errno==errorcode.ER_BAD_DB_ERROR:
        print ('Meter Number is Wrong')
    else:
        print(err)
else:
    cnx.close()




