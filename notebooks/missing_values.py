import pandas as pd
import numpy as np

def clining_missing_values(df):
      df['Self_Employed'] = df['Self_Employed'].replace(np.nan, 'No')
      df.loc[(df['CoapplicantIncome'] != 0) & (df['Married'].isna()), 'Married'] = 'Yes'
      df['Married'] = df['Married'].replace(np.nan, 'No')
      df['Dependents'] = df['Dependents'].replace(np.nan, '0')
      df['LoanAmount'] = df['LoanAmount'].replace(np.nan, 0)
      df['Credit_History'] = df['Credit_History'].replace(np.nan, 0)
      return df  