def divide_numbers():
    try:
        num1 = int(input("Enter First Number: "))
        num2 = int(input("Enter Second Number: "))

        result = num1 / num2

        print("Result =", result)

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

divide_numbers()