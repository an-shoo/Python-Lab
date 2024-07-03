def demonstrate_exceptions():
    try:
        a = int(input("Enter a number: "))
        b = int(input("Enter another number: "))
        result = a / b
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    else:
        print(f"The result is {result}")
    finally:
        print("Execution of the try-except block is complete.")

demonstrate_exceptions()
