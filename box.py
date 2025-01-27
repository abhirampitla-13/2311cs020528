import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Sample data (e.g., random numbers from a normal distribution)
data = np.random.randn(100)  # 100 random numbers from a standard normal distribution

# Create the box plot
sns.boxplot(data=data)

# Add a title and labels
plt.title('Box Plot of Random Data')
plt.xlabel('Data')

# Show the plot
plt.show()
