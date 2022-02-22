
# import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns
import numpy as np
# print('seaborn version\t:',sns.__version__)
# except Exception as e:
#     print(e)
# %matplotlib inline
# checking shape of dataset
df = pd.read_csv("EDA.csv")
# print(df.shape)
# (233154, 41) is the shape of dataset

# checking null values of the datasets

# print(df.isnull().sum())
# employment type has 7661 null values
# print(df['Employment.Type'].isnull().sum())

# remove constant feature
# as the feature which has zero variance will not be useful
def find_constant_features(dataFrame):
    const_features = []
    for column in list(dataFrame.columns):
        if dataFrame[column].unique().size < 2:
            const_features.append(column)
    return const_features
const_features = find_constant_features(df)
# print(const_features)
# ['MobileNo_Avl_Flag', 'Aadhar_flag', 'PAN_flag', 'VoterID_flag', 'Driving_flag', 'Passport_flag', 'loan_default'] are the constant feature so dropping that column from dataframe
# dropping all flag columns except loan default
df = df.drop(['MobileNo_Avl_Flag', 'Aadhar_flag', 'PAN_flag', 'VoterID_flag', 'Driving_flag', 'Passport_flag'], axis = 1)
n

# checking datatype of all columns
# print(df.dtypes)
df['Date.of.Birth'] = pd.to_datetime(df['Date.of.Birth'])
df['DisbursalDate']=pd.to_datetime(df['DisbursalDate'])
print(df.dtypes)

