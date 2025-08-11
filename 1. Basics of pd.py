##PANDAS##

import pandas as pd
from google.colab import files
uploaded = files.upload()
df = pd.read_csv('nyc_weather.csv')
df
print(df['Temperature'].max()) #get the maximum temperature
df['Temperature'].max()
df['EST'][df['Events'] == 'Rain']#to know which day it rains 
print(df['EST'][df['Events'] == 'Rain'])print(df['EST'][df['Events'] == 'Rain'])
print(df['WindSpeedMPH'].mean())
df.shape #total number of rows and columns
df.head() #to see some initial rows(default 5)
df.tail() #to see some last rows(default 5)
df[2:9]  #slicing
df.columns ##print column names of the table
df.Events  #print particular column data
df['Events'] #another way of accessing column (df.Events and these are same)
df[['EST','Events']] #get 2 or more columns data
df['Temperature'].min() #find the minimum temperature
df['Temperature'].describe() ##prints a set of values including the count,mean,std,min,25%, 50%, 75%, max
df[df.Temperature == df.Temperature.max()] ##select rows which has maximum temperature
df.Events[df.Temperature == df.Temperature.max()] ##select only 'Events' column which has maximum temperature
