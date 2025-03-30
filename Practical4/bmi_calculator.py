# Pseudocode:
# 1. Get user input for weight (kg) and height (m)
# 2. Calculate BMI using formula: weight / (height *height)
# 3. Classify into categories: obese (≥30), underweight (<18.5), normal otherwise
# 4. Output sentence with BMI value and classification

# Actual code:
# Get user input
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = weight/(height *height)

# Determine classification
if bmi < 18.5:
    category = "underweight"
elif 18.5 <= bmi < 30:
    category = "normal weight"
else:
    category = "obese"

# Generate output sentence
output =  "Your BMI is " + str(round(bmi, 1)) + ", which classifies you as " + category + "."
print(output)