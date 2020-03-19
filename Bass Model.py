#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np

df = pd.read_csv("2019_nCoV_data.csv")
df


# In[3]:


# The exact time is of no importance to me, so I'll split the Date column

df['Dates'] = pd.to_datetime(df['Date']).dt.date
df['Time'] = pd.to_datetime(df['Date']).dt.time
df


# In[4]:


# Since I'm only worried about confirmed cases and date of discovery, I shall drop the remaining columns.

df = df.drop(['Sno', 'Date', 'Province/State', 'Country', 'Last Update', 'Deaths', 'Recovered', 'Time'], axis = 1)
df


# In[5]:


# Now, I need my data to contain the total number of confirmed cases for each day in the given date range

df = df.groupby(df.Dates).sum().reset_index()
df


# In[5]:


df.rename(columns={'Dates':'Date'}, inplace=True)


# In[6]:


# Denoting each day by an integer timestamp for simplicity. This will also help me explain the Bass model to the reader later on

df['T'] = np.arange(0, len(df))


# In[7]:


x = 0
list = [x]
for i in range (0, len(df)-1):
    x += df.Confirmed[i]
    list.append(x)
    
ser = pd.Series(list)


# In[8]:


df.insert(3,'N', ser)


# In[9]:


x = 0
list = []
for i in range (0, len(df)):
    x = df.N[i] ** 2
    list.append(x)
    
ser = pd.Series(list)


# In[11]:


df.insert(4,'N_squared', ser)
df


# In[12]:


df.to_csv('Coronavirus_clean.csv')

