#!/usr/bin/env python
# coding: utf-8

# # Working with Database and Python task-1
1 . take a data set from attached URL https://archive.ics.uci.edu/ml/datasets/Car+Evaluation
2 . create a database called as cardataset
3 . create a table called as car with a column name given in dataset description
4 . Dump all the data into car table 
5 . try to check weather all the data is aviable inside your table or not 
6 . try to group all the data with COL1 AND count occurences of each and every record based on col1 value 
7 . Try to filter a record where col 3 value will be 4 .
8.  Try to update a col 3 value with 8 whereever you have value equal to 2 
9 . try to delete table 
10 .   Try to delete database
# In[1]:


import mysql.connector as conn


# In[2]:


mydb=conn.connect(host='localhost', user= 'root', passwd='mr.abhipotdar1997')


# In[3]:


cursor= mydb.cursor()


# In[4]:


cursor.execute('show databases')


# In[5]:


cursor.fetchall()


# 2 . create a database called as cardataset

# In[6]:


cursor.execute('create database cardataset')


# 3 . create a table called as car with a column name given in dataset description

# In[ ]:


cursor.execute('create table cardataset.car(col1 VARCHAR(10), col2 VARCHAR(10), col3 VARCHAR(10), col4 VARCHAR(10), col5 VARCHAR(10), col6 VARCHAR(10), col7 VARCHAR(10))')


# 4 . Dump all the data into car table 

# In[6]:


import csv
with open('car.data' , 'r') as f:
    car_data= csv.reader(f, delimiter = '\n')
    print(car_data)
    query = """ insert into cardataset.car(col1,col2,col3,col4,col5,col6,col7) values (%s,%s,%s,%s,%s,%s,%s)"""
    for i in car_data:
        split= str(i[0]).split(",")
        
        cursor.execute(query, split)
mydb.commit()


# 5 . try to check weather all the data is aviable inside your table or not 

# In[7]:


cursor.execute('select * from cardataset.car')


# In[8]:


cursor.fetchall()


# 6 . try to group all the data with COL1 AND count occurences of each and every record based on col1 value 

# In[9]:


cursor.execute("select count(col1), col1 from cardataset.car group by col1" )


# In[10]:


cursor.fetchall()


# 7 . Try to filter a record where col 3 value will be 4 .

# In[11]:


cursor.execute('select * from cardataset.car where col3=4')


# In[12]:


cursor.fetchall()


# 8.  Try to update a col 3 value with 8 whereever you have value equal to 2 

# In[13]:


cursor.execute('UPDATE cardataset.car SET col3="8" WHERE col3="2"')


# In[16]:


cursor.execute('select * from cardataset.car')


# In[17]:


cursor.fetchall()


# 9 . try to delete table 

# In[18]:


cursor.execute('delete from cardataset.car')


# In[20]:


cursor.execute('select * from cardataset.car ')


# In[21]:


cursor.fetchall()


# 10 .   Try to delete database

# In[23]:


cursor.execute('drop database cardataset')


# In[26]:


cursor.execute('show databases')


# In[27]:


cursor.fetchall()


# In[ ]:




