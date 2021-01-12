#!/usr/bin/env python
# coding: utf-8

# # Code by Colin Werkhoven & Matthew Turkenburg & Adnan Akbas & Ali safdari

# ##### Literature
# https://en.wikipedia.org/wiki/Rotation_matrix
# 
# https://medium.com/swlh/how-to-efficiently-loop-through-pandas-dataframe-660e4660125d

# ### The issue
# Currently, once the ActivPal device rotates in certain directions the associated X, Y, Z values also flip positions. This will cause problems in the future with creating accurate Machine Learning models because the data won't be consistent and will therefore not produce accurate results. 
# ### The solution
# This script will normalize all X, Y, Z value in the same format by looking at the `diceface` of each row to determine if the current format is correct or needs to be adjusted. 
# ### Idea
# Compare two values with the same `pal_diceFace`. Take their pal_time and check if the difference is greater then 15 seconds (current interval). If the interval is greater then 15, skip the comparison, if not apply our function that changes the X, Y, Z values to the same values as pal_diceFace 2.

# In[1]:


# Imports + Initializations

from helpers import pandas_helper as helper
from helpers import math_helper as mhp
from sensors.activpal import *

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

activpal = Activpal()


# #### Function by Colin & Adnan

# In[2]:


def opposite_of_number(number):
    return -number if number > 0 else abs(number)


# ### Converters written by Colin & Adnan
# All the converters convert xyz to the position of diceface 1
# #### Diceface 2 to 1

# In[15]:


# return x,y,z in this order
def convert_xyz_diceface_2_to_1(x, y, z):
    #(x, y, z)
    return (x, np.negative(z), y)


# #### Diceface 3 to 1

# In[16]:


# return x,y,z in this order
def convert_xyz_diceface_3_to_1(x,y,z):
    #(x y, z)
    return (y,  np.negative(z),  np.negative(x))


# #### Diceface 4 to 1

# In[17]:


# return x,y,z in this order
def convert_xyz_diceface_4_to_1(x, y, z):
    #(x, y, z)
    return (np.negative(y), np.negative(z), x)


# #### Diceface 5 to 1

# In[18]:


# return x,y,z in this order
def convert_xyz_diceface_5_to_1(x,y,z):
    #(x, y, z)
    return (np.negative(x), np.negative(z), np.negative(y) )


# #### Diceface 6 to 1

# In[19]:


# return x,y,z in this order
def convert_xyz_diceface_6_to_1(x, y, z):
    #(x, y, z)
    return (np.negative(x), y, np.negative(z))


# # Implementation by Adnan & Colin

# In[49]:


def correct_activpal_data(correspondent):
    activpal_15s_df = helper.read_csv_activpal1_15(correspondent)
    activpal_20_df = activpal.read_data(correspondent)
    
    activpal_20_df['pal_accX'] = mhp.convert_value_to_g(activpal_20_df['pal_accX'])
    activpal_20_df['pal_accY'] = mhp.convert_value_to_g(activpal_20_df['pal_accY'])
    activpal_20_df['pal_accZ'] = mhp.convert_value_to_g(activpal_20_df['pal_accZ'])
    
    activpal_20_df.drop(columns=['pal_time'], inplace=True)
    
    # This solve refence and duplicate issue
    corrected_activpal_df = activpal_20_df.copy()
        
    for index, diceface in zip(activpal_15s_df.index, activpal_15s_df['pal_diceFace']):

        previous_index = activpal_15s_df.index.get_loc(index) - 1
        prev_index = index - pd.DateOffset(seconds=15)

        if previous_index >= 0:
            prev_index = activpal_15s_df.index[previous_index]

        activpal_20_df_filtered = activpal_20_df.loc[prev_index:index]
        
        x = activpal_20_df_filtered['pal_accX']
        y = activpal_20_df_filtered['pal_accY']
        z = activpal_20_df_filtered['pal_accZ']
        
        if diceface == 1:
            new_x = x
            new_y = y
            new_z = z
        elif diceface == 2:
            new_x, new_y, new_z = convert_xyz_diceface_2_to_1(x, y, z)
        elif diceface == 3:
            new_x, new_y, new_z = convert_xyz_diceface_3_to_1(x, y, z)
        elif diceface == 4:
            new_x, new_y, new_z = convert_xyz_diceface_4_to_1(x, y, z)
        elif diceface == 5: 
            new_x, new_y, new_z = convert_xyz_diceface_5_to_1(x, y, z)
        elif diceface == 6:
            new_x, new_y, new_z = convert_xyz_diceface_6_to_1(x, y, z)

        
        corrected_activpal_df.loc[activpal_20_df_filtered.index, 'pal_accX'] = new_x
        corrected_activpal_df.loc[activpal_20_df_filtered.index, 'pal_accY'] = new_y
        corrected_activpal_df.loc[activpal_20_df_filtered.index, 'pal_accZ'] = new_z        
        corrected_activpal_df.loc[activpal_20_df_filtered.index, 'pal_diceFace'] = diceface


    corrected_activpal_df['pal_accX'] = mhp.convert_g_to_scaled_value(corrected_activpal_df['pal_accX'])
    corrected_activpal_df['pal_accY'] = mhp.convert_g_to_scaled_value(corrected_activpal_df['pal_accY'])
    corrected_activpal_df['pal_accZ'] = mhp.convert_g_to_scaled_value(corrected_activpal_df['pal_accZ'])

    return corrected_activpal_df


# #### Function by Adnan

# In[53]:


for directory in os.walk('../../data'):
    if directory[0] == '../../data':
        for respDirect in directory[1]:
            if respDirect not in ['output', 'throughput', 'Test data','.ipynb_checkpoints']:
                print("Extracting " + respDirect)
                
                new_df = correct_activpal_data(respDirect)
                print("Extracted "+ respDirect)
                new_df.to_csv('../../data/'+respDirect+'/activpal_20_diceface.csv', date_format='%Y-%m-%d %H:%M:%S:%f')
                print('saved' + '../../data/'+respDirect+'/activpal_20_diceface.csv')

                
print("Done normalizing data")


# In[38]:


new_df = correct_activpal_data('BMR099')


# In[50]:


new_df = correct_activpal_data('BMR099')


# In[12]:


activpal_15s_df = helper.read_csv_activpal1_15('BMR099')
activpal_20_df = activpal.read_data('BMR099')


# In[52]:


new_df.head()


# In[14]:


activpal_20_df.head()

