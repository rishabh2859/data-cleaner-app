"""
A python application that can take datasets and clean the data
- It should ask for datasets path and name
- it should check number of duplicats and remove all the duplicates 
- it should keep a copy of all the duplicates
- it should check for missing values 
- if any column that is numeric it should replace nulls with mean else it should drop that rows
- at end it should save the data as clean data and also return 
- duplicates records, clean_data 
"""
import random 
import os
import openpyxl
import xlrd
import csv
import time
import pandas as pd
def data_cleanser_app(datapath,dataname):
    sec=random.randint(1,10)
    print(f"Wait for {sec} seconds scanning filetype")
    time.sleep(sec)
    if not os.path.exists(f'{datapath}'):
        print("File does not exists")
    else:
     if datapath.endswith('.csv'):
        print("File type is csv")
        data=pd.read_csv(f'{datapath}')
     elif datapath.endswith('.xlsx'):
        print("File type is excel")
        data=pd.read_excel(f'{datapath}')
     else:
        print("Unknown filetype")
    sec1=random.randint(1,10)
    print(f"Wait for {sec1} seconds scanning duplicates")
    time.sleep(sec1)
    duplicates=data.duplicated()
    total_duplicates=duplicates.sum()
    print(f"Total {total_duplicates} duplicates detected")
    duplicated_data=data[duplicates]
    duplicated_data.to_csv(f'{dataname}_duplicates.csv',index=True)
    duplicate_freedata=data.drop_duplicates()
    sec2=random.randint(1,10)
    print(f"Wait for {sec2} seconds checking for null values")
    time.sleep(sec2)
    Null_values=data.isnull()
    total_null_columns=Null_values.sum()
    print(f"Null values by columns {total_null_columns}")
    total_nulls=Null_values.sum().sum()
    print(f"Total {total_nulls} null values/missing data detected")
    columns=duplicate_freedata.columns
    for column in columns:
       if duplicate_freedata[column].dtype in [float,int]:
          duplicate_freedata[column].fillna(duplicate_freedata[column].mean())
       else:
          duplicate_freedata=duplicate_freedata[duplicate_freedata[column].notna()]
    sec3=random.randint(1,10)
    print(f"Wait for {sec3} seconds exporting data")
    time.sleep(sec3)
    cleaned_data=duplicate_freedata.to_csv(f'{dataname}cleaned_data.csv',index=True)
    print("Thank you we are done")
    return 
user_input1=input("Enter file path")
user_input2=input("Enter the dataname")
data_cleanser_app(user_input1,user_input2)
