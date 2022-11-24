#!/usr/bin/env python
# coding: utf-8

# 

# In[66]:


import pymongo
import pandas as pd
import json


if __name__ == '__main__':
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    print(client)


# In[78]:


pf =pd.read_csv('carbon_nanotubes.csv')


# In[67]:


pf.head()  # find top 5 columns in the file


# In[68]:


pf.tail() # last five data


# In[69]:


pf.shape


# In[70]:


# convert csv file into jason beacuse  mongo db save a data in form of keys and values its call as dict 


# ## insert data (csv file)

# In[71]:


data = pf.to_dict(orient = "records")


# In[72]:


data


# In[73]:


db = client["file"]


# In[74]:


print(db)


# In[75]:


coll= db['csv']


# In[76]:


print(coll)


# In[77]:


coll.insert_many(data)


# ## update operation

# In[82]:


prev= {'col1':'2;1;0'}
nextt={'$set' :{'col2':'70000;0'}}


# In[83]:


coll.update_one(prev, nextt) #only one replace


# In[84]:


coll.update_many(prev, nextt) #in all data col2 are replace


# ## delete operation

# In[89]:


rec= {'col1':'2;1;0'}
coll.delete_one(rec) #delete one record


# In[90]:


coll.delete_many(rec) #delete all record


# ## find operation

# In[96]:


alldocs = coll.find({'col3':'724426;0'})
for items in alldocs:
    print(items)


# In[ ]:





# In[ ]:




