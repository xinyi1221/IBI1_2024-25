import matplotlib.pyplot as plt

# Pseudocode:
# 1. create a dictionary storing programming languages and their popularity
# 2. draw a bar graph
# 3. allow users to query the percentage of usage of a language

# Create a dictionary to store programming language data
language_popularity = {
    "JavaScript": 62.3,
    "HTML": 52.9,
    "Python": 51,
    "SQL": 51,
    "TypeScript": 38.5
}

# Drawing Bar Charts
plt.bar(language_popularity.keys(), language_popularity.values(), color=['blue', 'red', 'green', 'orange', 'purple'])
plt.xlabel("Programming Language")
plt.ylabel("Usage Percentage")
plt.title("Programming Language Popularity (2024)")
plt.show()

# Query the usage of a language (you can modify the language_to_check variable)
language_to_check = "Python"  # Modify this variable to query other languages
if language_to_check in language_popularity:
    print(f"The usage percentage of {language_to_check} is {language_popularity[language_to_check]}%")
else:
    print("Language not found.")
    
# Print the dictionary again after the query to show it matches the input
print("Programming Language Popularity Dictionary after query:")
print(language_popularity)