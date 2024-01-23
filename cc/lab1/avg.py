import matplotlib.pyplot as plt

# Data
userbases = ['UB1', 'UB2', 'UB3', 'UB4', 'UB5', 'UB6']



ESCE = [50.16,49.99,50.17,50.00,50.16,50.18]
RR = [50.18,49.97,50.17,50.03,50.14,50.19]
THR = [50.19,49.99,50.15,50.00,50.16,50.18]
# Plotting
plt.plot(userbases, ESCE, label='ESCE', marker='o')
plt.plot(userbases, RR, label='RR', marker='o')
plt.plot(userbases, THR, label='THR', marker='o')

# Adding labels and title
plt.xlabel('Userbases')
plt.ylabel('Values')
plt.title('Avg(ms)')

# Adding legend
plt.legend()

# Display the plot
plt.show()