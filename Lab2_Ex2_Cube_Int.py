# Cube of Integers

# Ask user how many elements in the array
while True:
    try:
        size_array = int(input("Enter the size of the array: "))
        print
        break
    except ValueError:
        print("Invalid input. Enter an integer.")

# Ask user to input the elements (separated by space)
while True:

    input_elements_string = str(input(f"Enter {size_array} elements separated by space: "))

    input_elements_int = input_elements_string.split()

    if len(input_elements_int) == size_array:
        integer_elements = [int(elements) for elements in input_elements_int]
    
        for number in integer_elements:
            print(number ** 3)
        break
    else:
        print(f"\nERROR: Enter exactly {size_array} elements.")
