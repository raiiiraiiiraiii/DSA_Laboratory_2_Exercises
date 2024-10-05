# Inverted Triangle

# Prompt user to input inverted triangle height
while True:
    try:
        height = int(input("\nEnter the height of the triangle: "))
        break
    except ValueError:
        print("Invalid input. Enter an integer.")

# Main program
for i in range(height, 0, -1):
    print('*' * i)