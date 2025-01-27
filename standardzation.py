from sklearn.preprocessing import StandardScaler
import numpy as np

# Sample data (for example, 5 data points and 3 features)
data = np.array([[10, 20, 30],
                 [20, 30, 40],
                 [30, 40, 50],
                 [40, 50, 60],
                 [50, 60, 70]])

# Initialize the StandardScaler
scaler = StandardScaler()

# Fit and transform the data (standardize the features)
standardized_data = scaler.fit_transform(data)

# Print the standardized data
print("Standardized Data using Scikit-learn:")
print(standardized_data)
