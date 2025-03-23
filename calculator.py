def calculator():
    # Display the calculator options for student to calculate 
    print("Simple Calculator")
    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    while True:
        # Prompt user for input
        choice = input("Enter choice (1/2/3/4) or 'q' to quit: ")
        
        # Exit the calculator if user enters 'q'
        if choice == 'q':
            print("Exiting calculator. Goodbye!")
            break
        
        # Check if the choice is a valid operation
        if choice in ('1', '2', '3', '4'):
            try:
                # Get two numbers from the user
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                # Perform the selected operation
                if choice == '1':
                    print(f"Result: {num1} + {num2} = {num1 + num2}")
                elif choice == '2':
                    print(f"Result: {num1} - {num2} = {num1 - num2}")
                elif choice == '3':
                    print(f"Result: {num1} * {num2} = {num1 * num2}")
                elif choice == '4':
                    # Prevent division by zero
                    if num2 != 0:
                        print(f"Result: {num1} / {num2} = {num1 / num2}")
                    else:
                        print("Error! Division by zero is not allowed.")
            except ValueError:
                # Handle non-numeric input
                print("Invalid input! Please enter numbers only.")
        else:
            # Handle invalid menu choices
            print("Invalid choice! Please enter a valid option.")

# Run the calculator function
calculator()

