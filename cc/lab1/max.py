import matplotlib.pyplot as plt

# Data
userbases = ['UB1', 'UB2', 'UB3', 'UB4', 'UB5', 'UB6']



ESCE = [64.39,64.89,61.92,62.63,60.36,63.14]
RR = [64.39,64.89,61.92,62.63,60.36,63.14]
THR = [64.39,64.89,61.92,62.63,60.36,63.14]
# Plotting
plt.plot(userbases, ESCE, label='ESCE', marker='o')
plt.plot(userbases, RR, label='RR', marker='o')
plt.plot(userbases, THR, label='THR', marker='o')

# Adding labels and title
plt.xlabel('Userbases')
plt.ylabel('Values')
plt.title('Max(ms)')

# Adding legend
plt.legend()

# Display the plot
plt.show()