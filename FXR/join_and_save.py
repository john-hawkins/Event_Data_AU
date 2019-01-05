import pandas as pd
import numpy as np

df1 = pd.read_csv('FXR.csv')
df2 = pd.read_csv('FXR2.csv')

df1['Date'] = pd.to_datetime(df1['Date'], format='%m/%d/%Y')
df2['Date'] = pd.to_datetime(df2['Date'], format='%m/%d/%Y')

# CREATE A NEW DATAFRAME WITH ALL DATES
maxdate = max(df2['Date'])
mindate = min(df1['Date'])

mydates = pd.date_range(mindate, maxdate)

newdf = pd.DataFrame()

for j in range(len(mydates)):
    newdf = newdf.append({'Date': mydates[j]}, ignore_index=True)

new_df = pd.merge(newdf, df,  how='left', left_on=['Department','Date'], right_on = ['Department','Date'])






