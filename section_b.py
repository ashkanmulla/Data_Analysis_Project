import pandas as pd


#step-1 -1.	Import both the Data Sets “Cust_Data.csv” & “Cust_Demo.csv”

cust_data = pd.read_csv("cust_data.csv")
#print(cust_data.columns)
#print(cust_data.head(10))
cust_demo = pd.read_csv("cust_demo.csv")
#print(cust_demo.columns)
#print(cust_demo.head(10))

#step-2 2.	Print the first 100 observations with “ID”, “SeriousDlqin2yrs” and “MonthlyIncome” variables from “Cust_Data” data set. 

cust_data_new_df = cust_data[['ID','SeriousDlqin2yrs','MonthlyIncome']]
# print(cust_data_new_df[0:100])

#step -3 3.	Convert “NumberOfDependents” and MonthlyIncome into Numeric variables and replace #N/A’s with missing values. 
# print(cust_demo.dtypes)
cust_demo['NumberOfDependents']=cust_demo['NumberOfDependents'].fillna(0)
cust_data['MonthlyIncome']=cust_data['MonthlyIncome'].fillna(0)
cust_demo['NumberOfDependents']=cust_demo['NumberOfDependents'].astype(int)
cust_data['MonthlyIncome']=cust_data['MonthlyIncome'].astype(int)

#data type of “NumberOfDependents” and MonthlyIncome changed to numeric and na are also filled
# print(cust_data['MonthlyIncome'])
# print("cust data type are",cust_data.dtypes)

#step-4 4.	Create new variable “Income bucket” using “Monthly Income” variable as follows.
#  a.	>1000000 
# b.	500000-1000000 
# c.200000-500000 
#d.	100000-200000 
#e.	<100000 
def column_mappping(cust_data):
    if cust_data['MonthlyIncome'] > 1000000:
        return 'a'
    elif cust_data['MonthlyIncome']>500000 and cust_data['MonthlyIncome']< 1000000:
        return 'b'

    elif cust_data['MonthlyIncome']>200000 and cust_data['MonthlyIncome']<500000:
        return 'c'

    elif cust_data['MonthlyIncome'] > 100000 and cust_data['MonthlyIncome']<200000 :
        return 'd'
    elif cust_data['MonthlyIncome']<100000:
        return 'e'
    else:
        return 'None'
Income_bucket = cust_data.apply(column_mappping, axis=1)
Income_bucket.name = 'Income_bucket'


cust_data = pd.concat([cust_data,Income_bucket],axis=1)
print(cust_data.columns)

#step-5 5.	Create new variable “Life_Stage_bucket” using “Age” variable as follows. 
# a.	Student: <22 
# b.	UnMarried_Employed: 23-27 
# c.	Married_with_Young_Kids: 27-40 
# d.	Pre_Retired: 40-60 
# e.	Retired: 60+ 
def column_mappping(cust_demo):
    if cust_demo['age'] < 22:
        return 'Student'
    elif cust_demo['age']>23 and cust_demo['age']<27:
        return 'Unamrried_Employed'

    elif cust_demo['age']>27 and cust_demo['age']<40:
        return 'Married_with_Young_Kids'

    elif cust_demo['age'] > 40 and cust_demo['age']<60:
        return 'Pre-Retired'
    elif cust_demo['age']>60:
        return 'Retired'
    else:
        return 'None'
Life_Stage_bucket = cust_demo.apply(column_mappping, axis=1)
Life_Stage_bucket.name = 'Life_Stage_bucket'
#print(Life_Stage_bucket)
cust_demo = pd.concat([cust_demo,Life_Stage_bucket],axis=1)
print(cust_demo.columns)
print("life stage bucket coulumn added to datframe")
#print(cust_demo.head(10))


#step6.	Sort the data using monthly income and create data set with top 20 customers. 
top_20_customers_monthly_income_datast= cust_data.sort_values(by='MonthlyIncome', ascending=True).reset_index(drop=True)[ :20]
# [ :20]
# top_20_customers_monthly_income =top_customers_monthly_income[ :20]
print(top_20_customers_monthly_income_datast)


# STEP 7 	Create new data set (customer_360) using “Cust_demo” to “Cust_data” data like below. 
# a.	Customers existed in “Cust_demo” and not existed in “Cust_data” 
# b.	Customers existed in “Cust_data” and not existed in “Cust_demo” 
# c.	Customers existed in both the tables. 
# d.	Customers existed in at least one table. 

# a.	Customers existed in “Cust_demo” and not existed in “Cust_data”
cust_in_cust_demo_not_in_cust_data = pd.merge(cust_data,cust_demo,on='ID',how ='left')
print(len(cust_in_cust_demo_not_in_cust_data))

# b.	Customers existed in “Cust_data” and not existed in “Cust_demo” 
cust_in_cust_dat_not_in_cust_demo = pd.merge(cust_data,cust_demo,on='ID',how ='right')
print(len(cust_in_cust_dat_not_in_cust_demo))

#C.CUSTOMER EXISTED IN BOTH TABLES
customer_in_both=pd.merge(cust_data,cust_demo,on='ID',how='outer')
print(len(customer_in_both))

#cCustomers existed in atleast one tables. 
customer_in_atleast_one= pd.merge(cust_data,cust_demo,on='ID')
print(len(customer_in_atleast_one))
customer_360 = pd.concat([cust_in_cust_demo_not_in_cust_data,cust_in_cust_dat_not_in_cust_demo,customer_in_both,customer_in_atleast_one],axis=0)
print(customer_360.columns)




#8.	From “Customer_360” data set, create two data sets “delinquent customers” and “non_delinquent_customers”
#  separately using “SeriousDlqin2yrs” variable). Also Export these data sets as “csv format” files. 

non_deliquent_customers=customer_360[customer_360['SeriousDlqin2yrs']==0]
non_deliquent_customers.to_csv('non_deliquent_customers.csv',header=True)
print(non_deliquent_customers)
deliquent_customers=customer_360[customer_360['SeriousDlqin2yrs']==1]
# print("dtype of del ",deliquent_customers.columns)
deliquent_customers.to_csv('deliquent_customers.csv',header=True)

#step9.	In “Customer_360” data set, split the “location” variable into two variables “City” & “State” 
#print(customer_360.columns)
customer_360[['city','state']] = customer_360['Location'].str.split(',',expand=True)
print(customer_360['city'].head(10))
print(customer_360['state'].head(10))

#
# STEP 10.	Create a single table with Top 10(in terms of monthly income) customers from each state.
top_10_monthly_income=customer_360.sort_values(['MonthlyIncome'],ascending=False).groupby('state').head(10) 
print(top_10_monthly_income)


# step 11 Find the distribution of “Life_Stage_bucket”, “Income_bucket” and SeriousDlqin2yrs. 

import matplotlib.pyplot as plt
# print(customer_360.columns)

customer_360['Life_Stage_bucket'].value_counts().hist(bins = 20)
plt.title(' Life_Stage_bucket Distribution')
plt.xlabel('x label')
plt.ylabel('y label')
# plt.show()

customer_360['SeriousDlqin2yrs'].value_counts().hist(bins = 20)
plt.title('SeriousDlqin2yrs Distribution')
plt.xlabel('x label')
plt.ylabel('y label')
plt.show()


customer_360['Income_bucket'].value_counts().hist(bins = 20)
plt.title('Income_bucket Distribution')
plt.xlabel('x label')
plt.ylabel('y label')
plt.show()



# 14.	Create format as follows and apply on Gender Variable. 
# a.	1- Male 
# b.	0- Female 
cust_demo['Gender']=cust_demo["Gender"].replace({"0": "Female", "1": "Male"})
print(cust_demo['Gender'].head(10))