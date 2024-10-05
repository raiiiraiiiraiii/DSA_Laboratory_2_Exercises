# Hollow Square

# Prompt user to input side lenght
length = int(input("Enter the side length of the square: "))

# Main function
for i in range (length):
    if i == 0 or i == (length-1):
        print('x' * length)
    else:
        print('x' + ' ' * (length-2) + 'x')