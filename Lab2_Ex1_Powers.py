# Calculation of Powers

# Main: Calculating the powers
def calculate_powers(base, exponent): 
    if exponent == 0:
        return 1
    else:
        return base * exponent(base, exponent - 1)

# Input the base
while True:
    try:
        base = int(input("Enter base number: "))
    except ValueError:
        print("Invalid input. Enter an integer.")
    break

# Input the exponent

# Display the result