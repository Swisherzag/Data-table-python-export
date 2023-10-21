import matplotlib.pyplot as plt
import scipy.stats as stats
# Generate a normal distribution
data = stats.norm.rvs(0, 1, 1000)
# Create a histogram
plt.hist(data, bins=25)
# Customize the plot
plt.title("Normal Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")
# Show the plot
plt.show()
# Please advise that anything under the bins of 5 is discarded