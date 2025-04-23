# dalys.py

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. Set the working directory to where your CSV file is located
os.chdir("C:/Users/ASUS/Downloads/IBI_lecture/IBI1_2024-25/Practical10")

# 2. Check current directory and files
print("Current working directory:", os.getcwd())
print("Files in this directory:", os.listdir())

# 3. Load the dataset
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

# 4. Show the “Year” column for the first 10 rows
print("\nYear column for the first 10 rows:")
print(dalys_data.iloc[0:10, 2])  # The third column is "Year"

# 5. Print the 10th row's country and year
print("\n10th row country and year:")
print("Country:", dalys_data.loc[9, "Entity"])
print("Year:", dalys_data.loc[9, "Year"])

# 6. Use Boolean indexing to select DALYs for the year 1990
dalys_1990 = dalys_data.loc[dalys_data["Year"] == 1990, "DALYs"]
print("\nSummary statistics for DALYs in 1990:")
print(dalys_1990.describe())

# 7. Compare average DALYs in UK and France
uk = dalys_data.loc[dalys_data.Entity == "United Kingdom", ["DALYs", "Year"]]
france = dalys_data.loc[dalys_data.Entity == "France", ["DALYs", "Year"]]

uk_mean = uk["DALYs"].mean()
france_mean = france["DALYs"].mean()

print("\nMean DALYs - United Kingdom:", uk_mean)
print("Mean DALYs - France:", france_mean)

if uk_mean > france_mean:
    print("The UK has a higher average DALYs.")
else:
    print("France has a higher average DALYs.")

# 8. Plot DALYs over time for the UK
plt.figure(figsize=(10, 5))
plt.plot(uk.Year, uk.DALYs, 'bo')  # 'bo' = blue circles
plt.xticks(rotation=90)
plt.title("DALYs Over Time in the United Kingdom")
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.grid(True)
plt.tight_layout()
plt.savefig("uk_dalys_plot.png")
plt.show()

# 9. Custom Question: Countries with DALYs greater than 650,000
print("\nCountries with DALYs greater than 650,000:")
high_dalys = dalys_data.loc[dalys_data.DALYs > 650000]
print(high_dalys)
