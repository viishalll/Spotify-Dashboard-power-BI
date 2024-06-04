#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv('spotify-2023.csv')


# In[3]:


df.head()


# In[4]:


df.tail()


# In[7]:


df.shape


# In[8]:


df


# In[11]:


df.info()


# In[12]:


print(f'Number of rows: {len(df.axes[0])}')
print(f'Number of columns: {len(df.axes[1])}')


# In[13]:


df.duplicated().sum()


# In[15]:


df.drop_duplicates(inplace=True) #dropping the duplicated values


# In[17]:


df.shape


# In[18]:


df.isnull().sum() #missing values/null values count


# In[22]:


#visualizing the missing valued using seaborn heatmap
plt.figure(figsize=(20,8))
sns.heatmap(df.isna().transpose(),
           cmap="YlGnBu",
           cbar_kws={'label':'missing Data'})

plt.title('missing values',fontsize=18)
plt.show()


# In[27]:


# Heatmap - Correlation Matrix
plt.figure(figsize=(12, 10))
correlation = df.corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()


# In[34]:


# Pie chart of tracks released per month
tracks_per_month = df['released_month'].value_counts()

plt.figure(figsize=(8, 8))
tracks_per_month.plot.pie(autopct='%1.1f%%', startangle=140, cmap='tab20')
plt.title('Pie Chart: Distribution of Tracks Released per Month')
plt.ylabel('')  # Hide the y-label
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




