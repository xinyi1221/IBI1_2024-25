import numpy as np
import matplotlib.pyplot as plt

# Set model parameters
beta = 0.3  # Infection probability
gamma = 0.05  # Recovery probability
vaccination_rate = 0.1  # 10% of population vaccinated

# Initialize 100x100 grid, all susceptible (0)
population = np.zeros((100, 100))

# Randomly vaccinate 10% of the population
num_vaccinated = int(100 * 100 * vaccination_rate)  # Total grid size is 100x100 = 10,000
vaccinated_indices = np.random.choice(100 * 100, num_vaccinated, replace=False)
vaccinated_rows, vaccinated_cols = np.unravel_index(vaccinated_indices, (100, 100))
population[vaccinated_rows, vaccinated_cols] = 3  # Vaccinated state

# Randomly select one non-vaccinated point to be infected
susceptible_indices = np.where(population == 0)  # Find all susceptible coordinates
outbreak_index = np.random.choice(len(susceptible_indices[0]))  # Pick one randomly
outbreak_row, outbreak_col = susceptible_indices[0][outbreak_index], susceptible_indices[1][outbreak_index]
population[outbreak_row, outbreak_col] = 1  # Set to infected

# Display initial state
fig = plt.figure(figsize=(6, 4), dpi=150)
plt.imshow(population, cmap='viridis', interpolation='nearest')
plt.title('Time 0')
plt.show()  # Show plot and wait for user to close it
plt.close(fig)

# Simulate for 100 time steps
for t in range(1, 101):
    # Find all infected individuals
    infected_rows, infected_cols = np.where(population == 1)
    
    # Lists to store new infections and recoveries
    new_infected_rows = []
    new_infected_cols = []
    to_recover_rows = []
    to_recover_cols = []
    
    # Process each infected individual
    for i, j in zip(infected_rows, infected_cols):
        # Check 8 neighbors
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if di != 0 or dj != 0:  # Exclude self
                    ni, nj = i + di, j + dj
                    # Check if neighbor is within grid and susceptible (0)
                    if 0 <= ni < 100 and 0 <= nj < 100 and population[ni, nj] == 0:
                        if np.random.random() < beta:
                            new_infected_rows.append(ni)
                            new_infected_cols.append(nj)
        
        # Check if infected individual recovers
        if np.random.random() < gamma:
            to_recover_rows.append(i)
            to_recover_cols.append(j)
    
    # Update grid
    if new_infected_rows:
        population[new_infected_rows, new_infected_cols] = 1  # New infections
    if to_recover_rows:
        population[to_recover_rows, to_recover_cols] = 2  # Recoveries
    
    # Display plot at specified time steps
    if t in [10, 50, 100]:
        fig = plt.figure(figsize=(6, 4), dpi=150)
        plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.title(f'Time {t}')
        plt.show()  # Show plot and wait for user to close it