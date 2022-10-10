# Global variables
RED = 'red'
BLUE = 'blue'
YELLOW = 'yellow'

# Get first color from the user.
color_1 = input('Enter the first primary color in lower case letters: ')

# Get second color from the user.
color_2 = input('Enter the second primary color in lower case letters: ')

# Check validity of first color.
if color_1 != RED and color_1 != BLUE and color_1 != YELLOW:
    print('Error: The first color you entered is invalid.')

# Check validity of second color.
elif color_2 != RED and color_2 != BLUE and color_2 != YELLOW:
    print('Error: The second color you entered is invalid.')

# Check if the two colors are the same.
elif color_1 == color_2:
    print('Error: The two colors you entered are the same.')

# Display the secondary color resulting from mixing the two colors.
else:
    # Determine secondary color if the first color is red.
    if color_1 == RED:
        if color_2 == BLUE:
            print('purple')
        else:  # Color 2 must be yellow
            print('orange')

    # Determine secondary color if first color is blue.
    elif color_1 == BLUE:
        if color_2 == RED:
            print('purple')
        else:  # Color 2 must be yellow.
            print('green')

    else:  # First color must be yellow.
        if color_2 == RED:
            print('orange')
        else:  # Color 2 must be blue.
            print('green')
