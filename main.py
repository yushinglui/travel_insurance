import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import preprocessing

df=pd.read_csv('travel_insurance.csv')
df.head()

df.info()

df=df.drop(['Gender'], axis=1)

df1 = df.groupby(by=["Destination"]).size().reset_index(name="counts")
df1.nlargest(15,['counts'])
df1['DestinationNew'] = np.where(df1['counts']>2200, df1['Destination'], 'Others')
fig = px.pie(df1, values='counts', names='DestinationNew', title='Popular destinations for the insured')
fig.update_traces(textposition='inside', textinfo='percent+label')
fig.show()

fig = plt.figure(figsize = (10, 5))
plt.hist(df['Age'],edgecolor='black')
plt.xlabel("Age")
plt.ylabel("Number of people")
plt.title("Age Distribution")
plt.show()

df1 = df.groupby(by=["Product Name"]).size().reset_index(name="counts")
df1.nlargest(15,['counts'])
df1['ProductNameNew'] = np.where(df1['counts']>5000, df1['Product Name'], 'Others')
fig = px.pie(df1, values='counts', names='ProductNameNew', title='Top 5 the most popluar plan')
fig.show()

df1=df.groupby(by=['Agency']).mean().reset_index()
fig = plt.figure(figsize = (10, 5))
plt.bar(df1['Agency'], df1['Commision (in value)'],edgecolor='black')
plt.xlabel("Agency")
plt.ylabel("Average of Commision")
plt.title("Average commision of agency")
plt.show()
