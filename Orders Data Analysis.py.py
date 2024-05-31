#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install kaggle')


# In[2]:


get_ipython().system('kaggle datasets download ankitbansal06/retail-orders -f orders.csv')


# In[3]:


#extract file from zip file
import zipfile
zip_ref = zipfile.ZipFile('orders.csv.zip') 
zip_ref.extractall() # extract file to dir
zip_ref.close() # close file


# In[4]:


# read the data from the file
import pandas as pd
df = pd.read_csv('orders.csv')
df.head(20)


# In[5]:


# handle all the null values
df['Ship Mode'].unique()


# In[6]:


# now handle null values other than nan
df = pd.read_csv('orders.csv', na_values=['Not Available', 'unknown'])
df['Ship Mode'].unique()


# In[7]:


# rename column names in lower case
df.rename(columns = {'Order Id':'order_id', 'City':'city'})


# In[8]:


# rename all the columns at once by onverting them into string objects
df.columns = df.columns.str.lower()
df.columns


# In[9]:


# replace whitespace with underscore in the each column
df.columns = df.columns.str.replace(' ','_')
df.columns


# In[10]:


df.head(5)


# In[11]:


# derive new columns discount, sales price and profit
df['discount'] = df['list_price']*df['discount_percent']*.01
df.head(5)


# In[12]:


df['sales_price'] = df['list_price'] - df['discount']
df.head(5)


# In[13]:


df['profit'] = df['sales_price'] - df['cost_price']
df.head(5)


# In[14]:


# data types in the data
df.dtypes


# In[15]:


# convert order_date from object data type to datetime
pd.to_datetime(df['order_date'], format='%Y-%m-%d')


# In[16]:


df['order_date'] = pd.to_datetime(df['order_date'], format='%Y-%m-%d')
df.dtypes


# In[17]:


# drop cost_price, list_price, discount_percent columns
df.drop(columns = ['discount_percent', 'list_price', 'cost_price'], inplace=True)
df.head(5)


# In[18]:


#load the data into sql server using replace option
import sqlalchemy as sal
engine = sal.create_engine('mssql://Sohail/master?driver=ODBC+DRIVER+17+FOR+SQL+SERVER')
conn=engine.connect()


# In[21]:


#load the data into sql server using append option
df.to_sql('df_orders', con=conn , index=False, if_exists = 'append')







