# Calculation of Powers

# Main: Calculating the powers
def calculate_powers(base, exponent): 
    if exponent == 0:
        return 1
    else:
        return base * calculate_powers(base, exponent - 1)

# Input the base
while True:
    try:
        input_base = int(input("Enter base number: "))
        break
    except ValueError:
        print("Invalid input. Enter an integer.")
    
# Input the exponent
while True:
    try:
        input_exponent = int(input("Enter exponent: "))
        break
    except ValueError:
        print("Invalid input. Enter an integer.")

powers_result = calculate_powers(input_base, input_exponent)

# Display the result
print(f"{input_base}^{input_exponent} = {powers_result}")