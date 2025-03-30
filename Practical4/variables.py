# Define walking and bus travel times
a = 15  # Time to walk to the bus stop (minutes)
b = 75  # Bus travel time (1 hour 15 minutes = 75 minutes)
c = a + b  # Total commute time (minutes)


# Define driving and walking times
d = 90  # Driving time (1 hour 30 minutes = 90 minutes)
e = 5   # Walking time after parking (minutes)
f = d + e  # Total commute time (minutes)

# Compare the two commuting methods
if c < f:
    quicker_method = "Bus is faster"
elif c > f:
    quicker_method = "Driving is faster"
else:
    quicker_method = "Both take the same time"

# Output results
print(f"Bus commute time: {c} minutes")
print(f"Driving commute time: {f} minutes")
print(f"The faster method is: {quicker_method}")

# Define Boolean variables
X = True
Y = False

# Define W variable (logical AND of X and Y)
W = X and Y

# Output the value of W
print(f"X = {X}, Y = {Y}, W = X and Y = {W}")

# Generate the truth table for X and Y
truth_table = [
    (False, False, False and False),
    (False, True, False and True),
    (True, False, True and False),
    (True, True, True and True)
]

# Print the truth table
print("Truth Table for W (X and Y):")
print("X     Y     W")
for row in truth_table:
    print(f"{row[0]}  {row[1]}  {row[2]}")

# Truth table content:
# X     Y     W
# False False False
# False True  False
# True  False False
# True  True  True