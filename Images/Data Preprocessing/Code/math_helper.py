import math
import numpy as np

#obsolete
def convert_to_acceleration_from_avg(row):
    return math.sqrt(row['pal_avgAccX'] ** 2 + row['pal_avgAccY'] ** 2 + row['pal_avgAccZ'] ** 2)

#Adnan akbas
#obsolete
def convert_to_acceleration(row):
    return math.sqrt(row['pal_accX'] ** 2 + row['pal_accY'] ** 2 + row['pal_accZ'] ** 2)

#use this instead
def to_mag_acceleration(accX, accY, accZ):
    return np.sqrt(accX ** 2 + accY ** 2 + accZ ** 2)

def calculate_met(vo2, kg):
    return vo2 / (3.5 * kg)

def calculate_bmi(weight, length_cm):
    return weight / ((length_cm / 100) ** 2)

#Adnan akbas 08/10/2020
def convert_value_to_g(value):
    return (value - 127) / 63

#Adnan akbas + Coling Werkhoven 27/10/2020
def convert_g_to_scaled_value(g):
    return (g * 63) + 127

#Ali Safdari 08/10/2020
def convert_value_to_acceleration(val):
    return ((val - 127) / 63) * 9.81    