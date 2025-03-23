import math

def advanced_calculator():
    # Display the calculator options
    print("Advanced Calculator")
    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power (x^y)")
    print("6. Square Root")
    print("7. Logarithm (log base 10)")
    print("8. Natural Logarithm (ln)")
    print("9. Sine (sin)")
    print("10. Cosine (cos)")
    print("11. Tangent (tan)")
    
    while True:
        # Prompt user for input
        choice = input("Enter choice (1-11) or 'q' to quit: ")
        
        # Exit the calculator if user enters 'q'
        if choice == 'q':
            print("Exiting calculator. Goodbye!")
            break
        
        # Perform operations based on choice
        if choice in ('1', '2', '3', '4', '5'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                if choice == '1':
                    print(f"Result: {num1} + {num2} = {num1 + num2}")
                elif choice == '2':
                    print(f"Result: {num1} - {num2} = {num1 - num2}")
                elif choice == '3':
                    print(f"Result: {num1} * {num2} = {num1 * num2}")
                elif choice == '4':
                    if num2 != 0:
                        print(f"Result: {num1} / {num2} = {num1 / num2}")
                    else:
                        print("Error! Division by zero is not allowed.")
                elif choice == '5':
                    print(f"Result: {num1}^{num2} = {math.pow(num1, num2)}")
            except ValueError:
                print("Invalid input! Please enter numbers only.")
        
        elif choice in ('6', '7', '8', '9', '10', '11'):
            try:
                num = float(input("Enter a number: "))
                
                if choice == '6':
                    print(f"Square root of {num} = {math.sqrt(num)}")
                elif choice == '7':
                    print(f"Log base 10 of {num} = {math.log10(num)}")
                elif choice == '8':
                    print(f"Natural log of {num} = {math.log(num)}")
                elif choice == '9':
                    print(f"sin({num}) = {math.sin(math.radians(num))}")
                elif choice == '10':
                    print(f"cos({num}) = {math.cos(math.radians(num))}")
                elif choice == '11':
                    print(f"tan({num}) = {math.tan(math.radians(num))}")
            except ValueError:
                print("Invalid input! Please enter a valid number.")
        else:
            print("Invalid choice! Please enter a valid option.")

# Run the advanced calculator function  yesssss it must work
advanced_calculator()
