class patients:
    def __init__(self, name, age, admission_date, medical_history):
        self.name = name
        self.age = age
        self.admission_date = admission_date
        self.medical_history = medical_history
    # function within this class 
    def print_details(self):
        print(f"{self.name}, {self.age}, {self.admission_date}, {self.medical_history}")

# Example call
p1 = patients("Cindy", 28, "2025-03-28", "No known allergies.")
p1.print_details()