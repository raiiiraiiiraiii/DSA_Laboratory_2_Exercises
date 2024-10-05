# Hollow Square

# Prompt user to input side lenght
while True:
    try:
        length = int(input("Enter the side length of the square: "))
        break
    except ValueError:
        print("Invalid input. Enter an integer")

# Main function
for i in range (length):
    if i == 0 or i == (length-1):
        print('x' * length)
    else:
        print('x' + ' ' * (length-2) + 'x')