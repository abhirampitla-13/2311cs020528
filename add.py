# Function to perform sum, multiplication, and division
def calculate_operations(num1, num2):
    # Sum of the two numbers
    sum_result = num1 + num2
    
    # Multiplication of the two numbers
    multiplication_result = num1 * num2
    
    # Division of the two numbers (handling division by zero)
    if num2 != 0:
        division_result = num1 / num2
    else:
        division_result = 'Undefined (division by zero)'
    
    # Return the results
    return sum_result, multiplication_result, division_result

# Input numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform calculations
sum_result, multiplication_result, division_result = calculate_operations(num1, num2)

# Print the results
print(f"Sum: {sum_result}")
print(f"Multiplication: {multiplication_result}")
print(f"Division: {division_result}")
