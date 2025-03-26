import matplotlib.pyplot as plt

# Pseudo-code:
# 1. Create a list to store population data for each country in the UK.
# 2. Create a list to store population data for the neighboring provinces of Zhejiang.
# 3. Sort the population data and print it
# 4. Draw two pie charts

# UK population data by country (in millions)
uk_countries = {"England": 57.11, "Wales": 3.13, "Northern Ireland": 1.91, "Scotland": 5.45}
# Population data of neighboring provinces of Zhejiang Province (in millions)
china_provinces = {"Zhejiang": 65.77, "Fujian": 41.88, "Jiangxi": 45.28, "Anhui": 61.27, "Jiangsu": 85.15}

# Sorting population data
sorted_uk_population = sorted(uk_countries.items(), key=lambda x: x[1])
sorted_china_population = sorted(china_provinces.items(), key=lambda x: x[1])

print("Sorted UK populations:", sorted_uk_population)
print("Sorted China populations:", sorted_china_population)

# Create a list to store population data for each country in the UK
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.pie(uk_countries.values(), labels=uk_countries.keys(), autopct='%1.1f%%', colors=['blue', 'red', 'green', 'purple'])
plt.title("UK Countries Population Distribution")

# Create a list to store population data for the neighboring provinces of Zhejiang
plt.subplot(1,2,2)
plt.pie(china_provinces.values(), labels=china_provinces.keys(), autopct='%1.1f%%', colors=['yellow', 'orange', 'cyan', 'pink', 'gray'])
plt.title("Zhejiang Neighboring Provinces Population Distribution")

plt.show()
