def arithmetic_operations():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print("Choose the operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choice = int(input("Enter the choice (1/2/3/4): "))

    if choice == 1:
        print(f"Result: {num1 + num2}")
    elif choice == 2:
        print(f"Result: {num1 - num2}")
    elif choice == 3:
        print(f"Result: {num1 * num2}")
    elif choice == 4:
        if num2 != 0:
            print(f"Result: {num1 / num2}")
        else:
            print("Error: Division by zero.")
    else:
        print("Invalid choice.")

arithmetic_operations()
