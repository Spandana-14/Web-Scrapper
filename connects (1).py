#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3
from importlib import reload
import sys
from imp import reload

#if sys.version[0] == '2':
    #reload(sys)
    #sys.setdefaultencoding("utf-8")

def connect(dbname):
    conn=sqlite3.connect(dbname)
    conn.execute("CREATE TABLE info_hotel (item_name TEXT, item_addr TEXT,item_rating INT ,item_ambiance TEXT )")
    print("Table created successfully")
    conn.close()

def insert_into_table(dbname,values):
    conn=sqlite3.connect(dbname)
    print("Inserted into table"+str(values))
    insert_sql="INSERT INTO info_hotel VALUES(?,?,?,?)"
    conn.execute(insert_sql,values)
    conn.commit()
    conn.close()
    
def get_Hotel_info(dbname):
    conn=sqlite3.connect(dbname)
    cur=conn.cursor()
    cur.execute("SELECT * FROM info_hotel ")
    table_data=cur.fetchall()
    for record in table_data:
        print(record)
    conn.close()


# In[ ]:




