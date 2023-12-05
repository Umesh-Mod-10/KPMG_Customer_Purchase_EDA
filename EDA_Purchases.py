# %% Importing all the necessary libraries:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
from sklearn.impute import SimpleImputer

# %% Loading the dataset:

data = pd.ExcelFile("C:/Users/umesh/OneDrive/Desktop/Umesh/Data Analysis/KPMG Internship/KPMG_VI_New_raw_data_update_final.xlsx")
tran = pd.read_excel(data, 'Transactions')
list = pd.read_excel(data, 'NewCustomerList')
demo = pd.read_excel(data, 'CustomerDemographic')
add = pd.read_excel(data, 'CustomerAddress')

# %% region Transactions:
# Getting basic Infos:

print(tran.info())
stats_Tran = tran.describe()
print(tran.isna().sum())
print(tran.shape)

# %% Formatting the date and time:

tran['transaction_date'] = pd.to_datetime(tran['transaction_date'])
print(tran.info())

# %% Checking the Nan values:

null = tran.isna().sum()
null = null[null != 0]
print(null)
nuller = pd.Series(null.index)

# %% Checking the relationship between brands:

sn.boxplot(data=tran, x="brand", y="list_price")
plt.show()

# %% Brands have a relation between them and list_price:

moder = SimpleImputer(strategy='most_frequent')
median = SimpleImputer(strategy='median')

# %% Replacing the Nan values:

for i in nuller:
    tran.loc[:, i] = moder.fit_transform(tran.loc[:, i].to_numpy().reshape((-1,1)))
print(tran.isna().sum())

# %% Grouping each category:

brand = (tran['brand'].value_counts())
online_order = (tran['online_order'].value_counts())
product_line = (tran['product_line'].value_counts())
product_class = (tran['product_class'].value_counts())
product_size = (tran['product_size'].value_counts())
features = ['brand', 'online_order', 'product_line', 'product_class', 'product_size']

# %% Plotting the graphs:

for i in features:
    plt.figure(figsize=(15,10))
    sn.countplot(data=tran, x=i, color="lightgreen", edgecolor='black')
    plt.title("The " + i + " Count")
    plt.show()

# %% Customer Demonstration:
# Getting the basic infos:

print(demo.info())
print(demo.isna().sum())
demo_stats = demo.describe()
print(demo.shape)

# %% Dealing with Nan values:

null_demo = demo.isna().sum()
null_demo = null_demo[null_demo != 0]

# %% Cleaning these Nan values:
# Let's ignore last_name, default DOB both as these are not that much necessary for Analysis:

demo.drop(columns=['default'], axis=1, inplace=True)
demo['last_name'].fillna(0, inplace=True)
demo['DOB'].fillna(0, inplace=True)

# %% Dealing with other Nan values:

demo.loc[:, 'job_title'] = moder.fit_transform(demo.loc[:, 'job_title'].to_numpy().reshape((-1,1)))
demo.loc[:, 'job_industry_category'] = moder.fit_transform(demo.loc[:, 'job_industry_category'].to_numpy().reshape((-1,1)))
demo.loc[:, 'tenure'] = median.fit_transform(demo.loc[:, 'tenure'].to_numpy().reshape((-1,1)))
print(demo.isna().sum())
print(demo.shape)

# %% Making the gender column uniform:

print(demo['gender'].value_counts())
demo['gender'] = demo['gender'].replace('F', "Female")
demo['gender'] = demo['gender'].replace('Femal', 'Female')
demo['gender'] = demo['gender'].replace('M', 'Male')
print(demo['gender'].value_counts())

# %% Getting plots based on different aspects of Past 3 years:

purchase_by_gender = demo.groupby('gender')['past_3_years_bike_related_purchases'].sum()
print(purchase_by_gender)
tenure_by_gender = demo.groupby('gender')['tenure'].sum()
print(tenure_by_gender)

# %% Getting plots to show this visually:

plt.figure(figsize=(8, 6))
purchase_by_gender.plot(kind='bar', color='skyblue')
plt.title('Total Bike Purchases by Gender')
plt.xlabel('Gender')
plt.ylabel('Total Purchases')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 6))
tenure_by_gender.plot(kind='bar', color='lightgreen')
plt.title('Total Bike Purchases by Tenure')
plt.xlabel('Gender')
plt.ylabel('Tenure')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# %% Getting plots based on Job Industry:

purchase_by_Indus = demo.groupby('job_industry_category')['past_3_years_bike_related_purchases'].sum()
print(purchase_by_Indus)
tenure_by_Indus = demo.groupby('job_industry_category')['tenure'].sum()
print(tenure_by_Indus)

# %% Getting plots to show this visually:

plt.figure(figsize=(8, 6))
purchase_by_Indus.plot(kind='bar', color='skyblue')
plt.title('Total Bike Purchases by Job Industry')
plt.xlabel('Job Industry')
plt.ylabel('Purchase 3 Years')
plt.xticks(rotation=90)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 6))
tenure_by_Indus.plot(kind='bar', color='lightgreen')
plt.title('Tenure by Job Industry')
plt.xlabel('Job Industry')
plt.ylabel('Tenure')
plt.xticks(rotation=90)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# %% Getting plots based on Wealth:

purchase_by_wealth = demo.groupby('wealth_segment')['past_3_years_bike_related_purchases'].sum()
print(purchase_by_wealth)
tenure_by_wealth = demo.groupby('wealth_segment')['tenure'].sum()
print(tenure_by_wealth)

# %% Getting plots to show this visually:

plt.figure(figsize=(8, 6))
purchase_by_wealth.plot(kind='bar', color='skyblue')
plt.title('Total Bike Purchases by Wealth')
plt.xlabel('Wealth')
plt.ylabel('Purchase 3 Years')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 6))
tenure_by_wealth.plot(kind='bar', color='lightgreen')
plt.title('Tenure by Wealth')
plt.xlabel('Wealth')
plt.ylabel('Tenure')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# %% By Customer Data:
# getting the basic infos:

print(list.info())
print(list.shape)
list_stats = list.describe()
print(list.isna().sum())

# %% Dropping unnecessary columns:

list.drop(columns=['Unnamed: 16', 'Unnamed: 17', 'Unnamed: 18', 'Unnamed: 19', 'Unnamed: 20'], axis=1, inplace=True)
print(list.info())

# %% Getting tenure by Statewise:

purchase_by_state = list.groupby('state')['past_3_years_bike_related_purchases'].sum()
print(purchase_by_state)
tenure_by_state = list.groupby('state')['tenure'].sum()
print(tenure_by_state)

# %% Getting plots to show this visually:

plt.figure(figsize=(8, 6))
purchase_by_state.plot(kind='bar', color='skyblue')
plt.title('Total Bike Purchases by State')
plt.xlabel('State')
plt.ylabel('Purchase 3 Years')
plt.xticks(rotation=90)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 6))
tenure_by_state.plot(kind='bar', color='lightgreen')
plt.title('Tenure by State')
plt.xlabel('State')
plt.ylabel('Tenure')
plt.xticks(rotation=90)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# %% Converting DOB into date and time:

list['DOB'] = pd.to_datetime(list['DOB'])
list['DOB'] = list['DOB'].dt.year
list['DOB'] = list['DOB'].astype(float)
list['DOB'] = 2023 - list['DOB']
list['DOB'] = list['DOB'].astype(float)

# %% Dealing with the Nan values of Age:

values = pd.cut(bins=4,x=list['DOB'].to_numpy())
print(values)

# %% Making it an categorical data:

bins = [20, 37, 53, 69, 85]
label = [0, 1, 2, 3]
list['DOB'] = pd.cut(list['DOB'], bins=bins, labels=label)

# %% Getting the visualization by Age:

purchase_by_age = list.groupby('DOB')['past_3_years_bike_related_purchases'].sum()
print(purchase_by_age)
tenure_by_age = list.groupby('DOB')['tenure'].sum()
print(tenure_by_age)

# %% Getting plots to show this visually:

plt.figure(figsize=(8, 6))
purchase_by_age.plot(kind='bar', color='skyblue')
plt.title('Total Bike Purchases by Age')
plt.xlabel('Age')
plt.ylabel('Purchase 3 Years')
plt.xticks(positions, labels, rotation=90)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 6))
tenure_by_age.plot(kind='bar', color='lightgreen', x=['20-37', '37-53', '53-69', '69-85'])
plt.title('Tenure by Age')
plt.xlabel('Age')
plt.ylabel('Tenure')
plt.xticks(rotation=90)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# %%
