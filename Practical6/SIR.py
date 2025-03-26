import numpy as np
import matplotlib.pyplot as plt

# Initialize population parameters
N = 10000  # Total population
I = 1      # Initially infected
S = N - I  # Initially susceptible
R = 0      # Initially recovered

# Infection and recovery rates
beta = 0.3   # Infection probability per contact
gamma = 0.05 # Recovery probability per time step

# Lists to store results
susceptible = [S]
infected = [I]
recovered = [R]

# Time simulation
time_steps = 1000

for _ in range(time_steps):
    new_infected = np.random.choice([0, 1], S, p=[1 - beta * (I / N), beta * (I / N)]).sum()
    new_recovered = np.random.choice([0, 1], I, p=[1 - gamma, gamma]).sum()

    S -= new_infected
    I += new_infected - new_recovered
    R += new_recovered

    susceptible.append(S)
    infected.append(I)
    recovered.append(R)

# Plot results
plt.figure(figsize=(8, 5), dpi=150)
plt.plot(susceptible, label="Susceptible", color="blue")
plt.plot(infected, label="Infected", color="red")
plt.plot(recovered, label="Recovered", color="green")
plt.xlabel("Time Steps")
plt.ylabel("Population")
plt.title("Stochastic SIR Model Simulation")
plt.legend()
plt.grid()
plt.show()
