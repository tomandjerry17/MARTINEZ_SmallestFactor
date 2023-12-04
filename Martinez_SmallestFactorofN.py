try:
    # Get user input for an integer
    num = int(input("Enter an integer >=2\n(Greater than or equal to 2)\n\t>> "))

    # Check if the input is greater than or equal to 2
    if num >= 2:
        smallestFactor = 0  # Initialize variable to store the smallest factor

        # Iterate through potential factors starting from 2 up to the square root of the number
        for i in range(2, int(num**0.5) + 1):

            if num % i == 0:
                smallestFactor = i
                break

        # Check if a factor was found
        if smallestFactor != 0:
            print("The smallest factor other than 1 for", num, "is", smallestFactor)
        else:
            print(num, "is a prime number.")
    else:
        print("Invalid input. Enter a number greater than 2.")

except ValueError:
    print("Invalid input. Please enter a valid integer.")
