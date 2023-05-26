import pandas as pd
import numpy as np

def features_eng(df):
     # Create total income column
     df['Total_Income'] = df['ApplicantIncome'] + df['CoapplicantIncome']
     df['Total_Income']=np.log(df['Total_Income'])
     df['LoanAmount']=np.log(df['LoanAmount'])
     #LoanAmount_per_Total_Income
     df["LoanAmount_per_Total_Income"] = round((df["LoanAmount"]/df["Total_Income"])*100,3)
     df["Dependents"] = df["Dependents"].replace("3+", 3).astype(int)
     df["Number_of_Family_Members"] = df["Dependents"] + 1 + (df["CoapplicantIncome"] > 0).astype(int)
     #LoanAmount_per_totalincome
     df["Total_Income_per_Family_Members"] = np.where(df["Dependents"], round((df["Total_Income"] / df["Number_of_Family_Members"]), 3), df["Total_Income"])
     df["LoanAmount_per_Loan_Amount_Term"] = round(df["LoanAmount"]/df["Loan_Amount_Term"]*100,2)
     df_eng = df.drop(columns=['Loan_ID','Gender','Married','ApplicantIncome','CoapplicantIncome','Dependents','Education','Property_Area','Self_Employed'])
     return df_eng    