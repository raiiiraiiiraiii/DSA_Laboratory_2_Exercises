# Calculation of Powers

# Main: Calculating the powers
def calculate_powers(base, exponent): 
    if exponent == 0:
        return 1
    else:
        return base * exponent(base, exponent - 1)

# Input the base
# Input the exponent
# Display the result