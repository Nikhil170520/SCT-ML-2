#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.cluster import KMeans as KM
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.preprocessing import StandardScaler as SS


# In[2]:


df=pd.read_csv(r'D:\Mall_Customers.csv')


# In[3]:


df


# In[4]:


df.describe()


# In[5]:


df.isnull().sum()


# In[6]:


fea=['Age','Annual Income (k$)','Spending Score (1-100)']


# In[7]:


sc=SS()
sc_df=sc.fit_transform(df[fea])


# In[8]:


km=KM(n_clusters=5)
km.fit(sc_df)


# In[9]:


df['cluster']=km.labels_


# In[10]:


# 3D Plot For KMeans Clustering
px.scatter_3d(df,x='Age',y='Annual Income (k$)',z='Spending Score (1-100)',color='cluster')



# In[11]:


# 2D Plot For Kmeans Clustering
plt.scatter(x=df['Age'],y=df['Annual Income (k$)'],c=df['cluster'])


# In[12]:


plt.scatter(x=df['Age'],y=df['Spending Score (1-100)'],c=df['cluster'])
plt.show()


# In[13]:


plt.scatter(x=df['Annual Income (k$)'],y=df['Spending Score (1-100)'],c=df['cluster'])
plt.show()

