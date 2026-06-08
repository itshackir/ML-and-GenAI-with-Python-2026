def palindrome(num):
    original = num
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    if original == reverse:
        return True
    else:
        return False

number = int(input("Enter a number: "))

if palindrome(number):
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")