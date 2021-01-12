#!/usr/bin/env python
# coding: utf-8

# #### By Colin Werkhoven

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[10]:


file_path = '../../data/activities_correspondents_combined.csv'


# In[11]:


data_set = pd.read_csv(file_path)


# In[13]:


# Count all duplicate activities and create a Dictionary
activities = data_set.pivot_table(index=['pal_activity_name'], aggfunc='size')
activities_as_dict = activities.to_dict()
print(activities_as_dict)


# In[20]:


plt.figure(figsize=(10,5))
plt.bar(activities_as_dict.keys(), activities_as_dict.values(), width=0.5)

plt.title('Activity Distribution')
plt.xlabel('Activity - Name')
plt.ylabel('Amount of rows per labelled activity')
plt.grid()
plt.show()


# In[ ]:




