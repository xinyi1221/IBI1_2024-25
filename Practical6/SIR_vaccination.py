import numpy as np
import matplotlib.pyplot as plt

# Initialize parameters
N = 10000
vaccination_rates = np.arange(0, 1.1, 0.1)  # 0% to 100% vaccinated
beta = 0.3
gamma = 0.05
time_steps = 1000

plt.figure(figsize=(8, 5), dpi=150)

for v_rate in vaccination_rates:
    V = int(N * v_rate)  # Vaccinated individuals
    S = max(N - V - 1, 0)  # Susceptible (ensure it's non-negative)
    I = 1  # Infected
    R = 0  # Recovered

    infected = [I]

    for _ in range(time_steps):
        if S > 0 and I > 0:
            new_infected = min(S, np.random.binomial(S, beta * (I / N)))  # Ensure valid range
        else:
            new_infected = 0

        new_recovered = min(I, np.random.binomial(I, gamma))  # Ensure valid range

        S -= new_infected
        I += new_infected - new_recovered
        R += new_recovered

        infected.append(I)

    plt.plot(infected, label=f"{int(v_rate * 100)}% vaccinated")

plt.xlabel("Time Steps")
plt.ylabel("Infected Population")
plt.title("Effect of Vaccination on Disease Spread")
plt.legend()
plt.grid()
plt.show()
