def add_numbers(num1, num2):
    """
    Function to add two numbers.
    
    Args:
        num1 (float): The first number to be added.
        num2 (float): The second number to be added.
    
    Returns:
        float: The sum of num1 and num2.
    """
    return num1 + num2

# Input two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Call the add_numbers function to calculate the sum
result = add_numbers(num1, num2)

# Display the result
print("The sum of {} and {} is: {}".format(num1, num2, result))

