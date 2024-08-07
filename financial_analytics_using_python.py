# -*- coding: utf-8 -*-
"""Financial Analytics Using Python.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10HI8ho0CZi3j0to2MKil2AoJaVJuDuPx

**"Financial Analytics Using Python"**

Objective:

To provide a comprehensive competitive analysis of the top 500 companies in India based on their market capitalization and quarterly sales, with the goal of identifying key market dynamics and actionable insights for improving business performance.

**Importing Libraries**
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""**Loading and Understanding the Dataset**"""

Datapath = '/content/Financial Analytics data.csv'

data = pd.read_csv(Datapath)
data.head()

data.shape

data.index

data.columns

data.info()

"""**Data Cleaning**"""

# Fill the empty spaces in 'Sales Qtr - Crore' with values from the unnamed column
data['Sales Qtr - Crore'] = data['Sales Qtr - Crore'].fillna(data.iloc[:, 4])

# Drop the unnamed column
data = data.drop(data.columns[4], axis=1)

# Create a mask for rows with null values in BOTH 'Market Capital - Crore' AND 'Sales Qtr - Crore'
mask = data[['Mar Cap - Crore', 'Sales Qtr - Crore']].isnull().all(axis=1)

# Set 'Company Name' and 'S.No.' to null for those rows
data.loc[mask, ['Name', 'S.No.']] = None

data.info()

Data = data.dropna(subset=['S.No.', 'Name', 'Mar Cap - Crore'])

Data.info()

# Calculate skewness of 'Sales Qtr - Crore' column
sales_skewness = Data['Sales Qtr - Crore'].skew()

print(sales_skewness)

Data['Sales Qtr - Crore'] = Data['Sales Qtr - Crore'].fillna(Data['Sales Qtr - Crore'].median())

Data.isnull().sum()

# Drop the 'S.No.' column
Data = Data.drop('S.No.', axis=1)

# Rename the columns
Data = Data.rename(columns={'Mar Cap - Crore': 'Market Capital', 'Sales Qtr - Crore': 'Quarter Sales'})

# Display the modified DataFrame (optional)
Data.head()

Data.info()

"""**Data Analysis and Visualization**"""

Data.describe()

sns.distplot(Data['Market Capital'])

sns.distplot(Data['Quarter Sales'])

"""**Top and Bottom 5 Companies based on Market Capitalization**"""

Data.nlargest(5, 'Market Capital')

Data.nsmallest(5, 'Market Capital')

"""**Top and Bottom 5 Companies based on Quarter Sales**"""

Data.nlargest(5, 'Quarter Sales')

Data.nsmallest(5, 'Quarter Sales')

# Calculate total market capitalization
total_market_cap = Data['Market Capital'].sum()

# Get the top 10 companies by market capitalization
top_10_market_cap = Data.nlargest(10, 'Market Capital')

# Calculate market share for top 10 companies
top_10_market_cap_shares = top_10_market_cap['Market Capital'] / total_market_cap

# Calculate the market share of other companies
other_market_cap_share = 1 - top_10_market_cap_shares.sum()

# Combine the market shares
sizes = top_10_market_cap_shares.tolist() + [other_market_cap_share]

# Create a list of colors, highlighting each company
colors = ['yellow', 'green', 'red', 'purple', 'orange', 'brown', 'pink', 'gray', 'cyan', 'blue', 'violet']

# Create the pie chart
labels = top_10_market_cap['Name'].tolist() + ['Others']
plt.pie(
    sizes,
    labels=labels,
    autopct='%1.1f%%',
    startangle=90,
    colors=colors,
    pctdistance=0.85,  # Adjusts the position of the percentage labels
    labeldistance=1.1  # Adjusts the position of the labels
)
plt.title('Market Capital Share Distribution')
plt.axis('equal')

# Add a legend on the side
plt.legend(labels, loc="center left", bbox_to_anchor=(1, 0.5))

# Display the chart
plt.show()

# Calculate total sales
total_sales = Data['Quarter Sales'].sum()

# Get the top 10 companies by quarter sales
top_10_sales = Data.nlargest(10, 'Quarter Sales')

# Calculate sales share for top 10 companies
top_10_sales_shares = top_10_sales['Quarter Sales'] / total_sales

# Calculate the sales share of other companies
other_sales_share = 1 - top_10_sales_shares.sum()

# Combine the sales shares
sizes = top_10_sales_shares.tolist() + [other_sales_share]

# Create a list of colors, highlighting each company
colors = ['yellow', 'green', 'red', 'purple', 'orange', 'brown', 'pink', 'gray', 'cyan', 'blue', 'violet']

# Create the pie chart
labels = top_10_sales['Name'].tolist() + ['Others']
plt.pie(
    sizes,
    labels=labels,
    autopct='%1.1f%%',
    startangle=90,
    colors=colors,
    pctdistance=0.85,  # Adjusts the position of the percentage labels
    labeldistance=1.1  # Adjusts the position of the labels
)
plt.title('Sales Share Distribution')
plt.axis('equal')

# Add a legend on the side
plt.legend(labels, loc="center left", bbox_to_anchor=(1, 0.5))

# Display the chart
plt.show()

# Create a scatter plot
plt.figure(figsize=(10, 6))  # Adjust figure size if needed
sns.scatterplot(x='Market Capital', y='Quarter Sales', data=Data)
plt.title('Relationship between Market Capital and Quarter Sales')
plt.xlabel('Market Capital')
plt.ylabel('Quarter Sales')
plt.grid(True)  # Add a grid for better visualization
plt.show()

correlation = Data['Market Capital'].corr(Data['Quarter Sales'])
print("Correlation coefficient:", correlation)

"""**Conclusion**

The analysis of India's top 500 companies reveals a significant concentration of market power within the top 10 firms, both in terms of market capitalization and quarterly sales. These leading companies dominate the market, accounting for a substantial share of the total market value and sales revenue, while the bottom companies hold minimal shares. The positive correlation coefficient of 0.6 between market capitalization and quarterly sales suggests that companies with higher market value generally experience higher sales, though other factors also contribute to these metrics.

Given these insights, market leaders should leverage their dominant position to drive further innovation and expansion, while smaller companies should focus on niche markets and unique value propositions to differentiate themselves.
"""