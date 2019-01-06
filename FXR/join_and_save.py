import pandas as pd
import numpy as np

df1 = pd.read_csv('FXR1.csv')
df2 = pd.read_csv('FXR2.csv')

df1['DATE'] = pd.to_datetime(df1['DATE'], format='%d-%b-%Y')
df2['DATE'] = pd.to_datetime(df2['DATE'], format='%d-%b-%Y')

# CREATE A NEW DATAFRAME WITH ALL DATES
maxdate = max(df2['DATE'])
mindate = min(df1['DATE'])

mydates = pd.date_range(mindate, maxdate)

newdf = pd.DataFrame()

for j in range(len(mydates)):
    newdf = newdf.append({'DATE': mydates[j]}, ignore_index=True)

join_df = pd.concat([df1,df2], ignore_index=True)

new_df = pd.merge(newdf, join_df,  how='left', left_on=['DATE'], right_on = ['DATE'])

new_df.to_csv('FXR_Joined_Processed.csv', sep=',', encoding='utf-8', index=False, header=True)

