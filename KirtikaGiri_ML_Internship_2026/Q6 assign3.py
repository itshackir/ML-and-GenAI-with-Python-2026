def fibonacci(n):
    first = 0
    second = 1

    print("Fibonacci Series:")

    for i in range(n):
        print(first, end=" ")

        next_term = first + second
        first = second
        second = next_term

terms = int(input("Enter number of terms: "))

fibonacci(terms)