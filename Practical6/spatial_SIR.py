import numpy as np
import matplotlib.pyplot as plt

# Grid size
size = 100
population = np.zeros((size, size))  # 0 = susceptible, 1 = infected, 2 = recovered

# Initial infection
outbreak = np.random.randint(0, size, 2)
population[outbreak[0], outbreak[1]] = 1  # Infect one random person

# Infection and recovery parameters
beta = 0.3  # Infection probability per contact
gamma = 0.05  # Recovery probability per time step
time_steps = 100  # Ensure full 100 steps

# Simulation loop
for t in range(time_steps + 1):  # Ensure we reach t = 100
    new_population = population.copy()
    
    for x in range(size):
        for y in range(size):
            if population[x, y] == 1:  # Infected
                # Infect neighbors
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if (dx == 0 and dy == 0) or not (0 <= x + dx < size and 0 <= y + dy < size):
                            continue
                        if population[x + dx, y + dy] == 0 and np.random.rand() < beta:
                            new_population[x + dx, y + dy] = 1
                # Recover
                if np.random.rand() < gamma:
                    new_population[x, y] = 2

    population = new_population.copy()

    # Plot at key time steps, including t=100
    if t in [0, 10, 50, 100]:  
        plt.figure(figsize=(6, 4), dpi=150)
        plt.imshow(population, cmap="viridis", interpolation="nearest")
        plt.title(f"Time Step {t}")
        plt.colorbar(label="State (0=Susceptible, 1=Infected, 2=Recovered)")
        plt.show()
