def start():
    print("Welcome to the Python Calculator!")
    print("Enter 'END' at any time to exit.")
    
    while True:
        # Ask the user to input the operation
        operation = input("Choose an operation (add, subtract, multiply, divide): ").lower()
        
        if operation == "end":
            print("Calculator exiting. Goodbye!")
            break  # End the loop if the user enters 'END'

        # Validating the operation
        if operation not in ["add", "subtract", "multiply", "divide"]:
            print("Invalid operation. Please try again.")
            continue  # Go back to the start of the loop

        try:
            # Get the numbers from the user
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            # Perform the calculation
            if operation == "add":
                print(f"The result is: {num1 + num2}")
            elif operation == "subtract":
                print(f"The result is: {num1 - num2}")
            elif operation == "multiply":
                print(f"The result is: {num1 * num2}")
            elif operation == "divide":
                # Handle division by zero
                if num2 == 0:
                    print("Error: Cannot divide by zero!")
                else:
                    print(f"The result is: {num1 / num2}")
        except ValueError:
            print("Invalid input. Please enter numeric values only.")

# Start the calculator
start()
