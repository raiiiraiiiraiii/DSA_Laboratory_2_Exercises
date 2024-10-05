# Inverted Triangle

# Prompt user to input inverted triangle height
height = int(input("Enter the height of the triangle: "))

# Main program
for i in range(height, 0, -1):
    print('*' * i)