# -*- coding: utf-8 -*-
"""Ajay and friends.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vJpGZGE_tHny--bmMjaNDLkQO3fIFQv0

Showing columns
"""

import pandas as pd
df = pd.read_excel("/content/MF_Behavior.xlsx")
print("Columns in the dataset:")
print(df.columns)

"""Maximum Likelihood model"""

import pandas as pd
import statsmodels.api as sm
df = pd.read_excel("/content/MF_Behavior.xlsx")
dependent_variable_column = 'Longevity'
independent_variable_columns = ['Female', 'Age', 'Income', 'ProfManage',
                                 'Diversification', 'Affordability', 'Liquidity',
                                 'Growth', 'Trustworthiness', 'Technology',
                                 'Integrity', 'BrandValue', 'AUM']
X = sm.add_constant(df[independent_variable_columns])
model = sm.OLS(df[dependent_variable_column], X)
result = model.fit()

# Display the results
print(result.summary())

"""Plots"""

import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
# Load the dataset
df = pd.read_excel("/content/MF_Behavior.xlsx")
# Define the actual column names
dependent_variable_column = 'Longevity'
independent_variable_columns = ['Female', 'Age', 'Income', 'ProfManage',
                                 'Diversification', 'Affordability', 'Liquidity',
                                 'Growth', 'Trustworthiness', 'Technology',
                                 'Integrity', 'BrandValue', 'AUM']
X = sm.add_constant(df[independent_variable_columns])
model = sm.OLS(df[dependent_variable_column], X)
result = model.fit()
plt.scatter(df[dependent_variable_column], result.fittedvalues)
plt.xlabel('Observed Values')
plt.ylabel('Predicted Values')
plt.title('Observed vs. Predicted Values')
plt.show()
plt.scatter(result.fittedvalues, result.resid)
plt.xlabel('Fitted Values')
plt.ylabel('Residuals')
plt.title('Residual Plot')
plt.axhline(y=0, color='r', linestyle='--')  # Add a horizontal line at y=0
plt.show()

"""Unsupervised Learning and Clustering"""

# Import necessary libraries
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
file_path = '/content/MF_Behavior.xlsx'
df = pd.read_excel(file_path)
print(df.head())
features = df[['Longevity', 'Female', 'Age', 'Income', 'ProfManage',
               'Diversification', 'Affordability', 'Liquidity', 'Growth',
               'Trustworthiness', 'Technology', 'Integrity', 'BrandValue', 'AUM']]
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)
num_clusters = 3
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
df['Cluster'] = kmeans.fit_predict(features_scaled)
sns.scatterplot(x='Age', y='Income', hue='Cluster', data=df, palette='viridis')
plt.title('K-means Clustering')
plt.show()
cluster_centers = scaler.inverse_transform(kmeans.cluster_centers_)
cluster_centers_df = pd.DataFrame(cluster_centers, columns=features.columns)
print("Cluster Centers:")
print(cluster_centers_df)

"""Foundation of Supervised Learning Model"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
file_path = '/content/MF_Behavior.xlsx'
df = pd.read_excel(file_path)
features = df[['Longevity', 'Female', 'Age', 'Income', 'ProfManage',
               'Diversification', 'Affordability', 'Liquidity', 'Growth',
               'Trustworthiness', 'Technology', 'Integrity', 'BrandValue']]
target = df['AUM']
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)
print(f'Mean Squared Error: {mse}')

"""Plots"""

import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(10, 6))
sns.scatterplot(x=y_test, y=predictions)
plt.xlabel('Actual AUM')
plt.ylabel('Predicted AUM')
plt.title('Actual vs Predicted AUM')
plt.show()
residuals = y_test - predictions
plt.figure(figsize=(10, 6))
sns.scatterplot(x=y_test, y=residuals)
plt.axhline(y=0, color='r', linestyle='--', linewidth=2)
plt.xlabel('Actual AUM')
plt.ylabel('Residuals')
plt.title('Residual Plot')
plt.show()

"""Decision Trees"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
file_path = '/content/MF_Behavior.xlsx'
df = pd.read_excel(file_path)
features = df[['Longevity', 'Female', 'Age', 'Income', 'ProfManage',
               'Diversification', 'Affordability', 'Liquidity', 'Growth',
               'Trustworthiness', 'Technology', 'Integrity', 'BrandValue']]
target = df['AUM']
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)
model = DecisionTreeRegressor(random_state=42)
model.fit(X_train, y_train)
predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)
print(f'Mean Squared Error: {mse}')

"""Plots"""

from sklearn.tree import plot_tree

# Visualize the Decision Tree
plt.figure(figsize=(15, 10))
plot_tree(model, feature_names=features.columns, filled=True, rounded=True)
plt.title('Decision Tree for AUM Prediction')
plt.show()

"""Neural Network"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from sklearn.metrics import mean_squared_error
file_path = '/content/MF_Behavior.xlsx'
df = pd.read_excel(file_path)
features = df[['Longevity', 'Female', 'Age', 'Income', 'ProfManage',
               'Diversification', 'Affordability', 'Liquidity', 'Growth',
               'Trustworthiness', 'Technology', 'Integrity', 'BrandValue']]
target = df['AUM']
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)
X_train, X_test, y_train, y_test = train_test_split(features_scaled, target, test_size=0.2, random_state=42)
model = Sequential()
model.add(Dense(64, input_dim=X_train.shape[1], activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='linear'))
model.compile(optimizer=Adam(learning_rate=0.001), loss='mean_squared_error')
model.fit(X_train, y_train, epochs=50, batch_size=32, validation_data=(X_test, y_test))
predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)
print(f'Mean Squared Error: {mse}')

"""plots"""

import matplotlib.pyplot as plt
import seaborn as sns
result_df = pd.DataFrame({'Actual': y_test, 'Predicted': predictions.flatten()})
# Scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Actual', y='Predicted', data=result_df)
plt.title('Actual vs. Predicted AUM using Neural Network')
plt.xlabel('Actual AUM')
plt.ylabel('Predicted AUM')
plt.show()

"""plot 2"""

result_df = result_df.sort_values(by='Actual')
# Line plot
plt.figure(figsize=(12, 6))
plt.plot(result_df['Actual'], label='Actual AUM', marker='o')
plt.plot(result_df['Predicted'], label='Predicted AUM', marker='o')
plt.title('Actual vs. Predicted AUM using Neural Network')
plt.xlabel('Observations')
plt.ylabel('AUM')
plt.legend()
plt.show()