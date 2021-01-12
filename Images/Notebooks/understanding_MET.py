#!/usr/bin/env python
# coding: utf-8

# #### By Colin Werkhoven

# # Calculating MET value with Oxygen intake

# #### Imports + Initialization

# In[2]:


from helpers import pandas_helper as helper

correspondent = 'BMR002'
# correspondent = 'BMR004'
activity = 'lopen'


# ### MET value calculation

# In[3]:


def calculate_met_with_oxygen(vo2, kg):
    return vo2 / (3.5 * kg)


# ### Get values
# Get the vyntus file and details of the correspondent
# 
# Sorting the vyntus data ascending

# In[4]:


vyntus_df = helper.read_csv_vyntus(correspondent)
vyntus_df.sort_index(inplace=True)
# vyntus_df = vyntus_df.loc['2019-09-16 15:12:00':'2019-09-16 15:17:00']
# vyntus_df = vyntus_df.loc['2019-10-10 15:36:00':'2019-10-10 15:41:00']
vyntus_df = vyntus_df[['vyn_VO2', 'vyn_activity']]

respondents_df = helper.read_csv_respondents()
respondent_details = respondents_df.loc[float(correspondent[3:6])]


# ### Printing head walking data ascending

# In[5]:


print(vyntus_df.head())


# ### Adding the MET value and weight to the vyntus rows
# First we need to assign the weight/gewicht of the correspondent to the Vyntus dataframe  

# In[6]:


vyntus_df['weight'] = respondent_details['gewicht']
vyntus_df['MET'] = [calculate_met_with_oxygen(vo2, weight) for vo2, weight in zip(vyntus_df['vyn_VO2'], vyntus_df['weight'])]
weight = respondent_details['gewicht']
length = respondent_details['lengte']
bmi = weight / (length * length)
print(bmi*10000)
print(vyntus_df.describe())
vyntus_df

