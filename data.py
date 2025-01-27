# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Load dataset (example: CSV file)
df = pd.read_csv('your_dataset.csv')

# 1. Handling missing values
# Example: Fill missing numerical values with the mean and categorical with the mode
df.fillna(df.mean(), inplace=True)  # For numerical columns
df.fillna(df.mode().iloc[0], inplace=True)  # For categorical columns

# 2. Encoding categorical variables
# Example: Encoding categorical variables using Label Encoding
label_encoder = LabelEncoder()

# Apply label encoding to a specific column
df['categorical_column'] = label_encoder.fit_transform(df['categorical_column'])

# 3. Feature scaling (standardization) - Scaling numerical columns
scaler = StandardScaler()

# Assume 'numeri
