import matplotlib.pyplot as plt
import numpy as np

# Sample data (e.g., random numbers from a normal distribution)
data = np.random.randn(1000)  # 1000 random numbers from a standard normal distribution

# Create the histogram
plt.hist(data, bins=30, edgecolor='black')  # 30 bins and black edges for clarity

# Adding title and labels
plt.title('Histogram of Random Data')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Show the plot
plt.show()
