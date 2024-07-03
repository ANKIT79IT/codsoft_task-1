# our first program making calculator.
def calculate(num1, num2, operation):
  if operation == "+":
    return num1 + num2
  elif operation == "-":
    return num1 - num2
  elif operation == "*":
    return num1 * num2
  elif operation == "/":
    return num1 / num2
  else:
    print("Invalid operation")
    return None
# Get user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")
# Perform the calculation and display the result
result = calculate(num1, num2, operation)
if result:
  print(f"The result is: {result}")
