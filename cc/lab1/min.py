import matplotlib.pyplot as plt

# Data
userbases = ['UB1', 'UB2', 'UB3', 'UB4', 'UB5', 'UB6']



ESCE = [40.89,38.64,37.66,37.39,39.36,38.90]
RR = [40.89,38.64,37.66,37.39,39.36,38.90]
THR = [40.89,38.64,37.66,37.39,39.36,38.90]
# Plotting
plt.plot(userbases, ESCE, label='ESCE', marker='o')
plt.plot(userbases, RR, label='RR', marker='o')
plt.plot(userbases, THR, label='THR', marker='o')

# Adding labels and title
plt.xlabel('Userbases')
plt.ylabel('Values')
plt.title('Min(ms)')

# Adding legend
plt.legend()

# Display the plot
plt.show()