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
        break
    except ValueError:
        print("Invalid input. Enter an integer.")
    
# Input the exponent
while True:
    try:
        exponent = int(input("Enter exponent: "))
        break
    except ValueError:
        print("Invalid input. Enter an integer.")
    
# Display the result