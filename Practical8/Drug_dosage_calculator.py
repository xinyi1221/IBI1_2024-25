def calculate_dose(weight, strength):
    
    errors = []

    # Check the weight range
    if weight < 10 or weight > 100:
        errors.append("Weight must be between 10 and 100 kg.")
    
    # Checking drug concentrations for validity
    if strength not in ['120mg/5ml', '250mg/5ml']:
        errors.append("Invalid paracetamol strength. Choose '120mg/5ml' or '250mg/5ml'.")

    # If there are any errors, return an error message (can be combined into one)
    if errors:
        return "Error(s): " + "; ".join(errors)

    # normal calculation
    if strength == '120mg/5ml':
        concentration = 120 / 5
    else:
        concentration = 250 / 5
    
    dose_mg = 15 * weight
    volume_ml = dose_mg / concentration
    return volume_ml

# Example call
print(calculate_dose(26, '120mg/5ml'))
