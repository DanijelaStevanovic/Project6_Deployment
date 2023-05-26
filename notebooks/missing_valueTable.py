import pandas as pd
import numpy as np


# missing values percent in columns
def missing_values_table(df):
        '''function that checks dataframe for missing values and returns a table with the results'''
        mis_val = df.isnull().sum()
        mis_val_percent = 100 * df.isnull().sum() / len(df)
        mis_val_table = pd.concat([mis_val, mis_val_percent], axis=1)
        mis_val_table_ren_columns = mis_val_table.rename(
        columns = {0 : 'Missing Values', 1 : '% of Total Values'})
        print(mis_val_table_ren_columns)



        