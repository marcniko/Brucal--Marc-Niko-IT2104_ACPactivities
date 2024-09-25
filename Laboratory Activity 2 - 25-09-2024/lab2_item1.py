def is_palindrome(number):
    num_str = str(number)
    if num_str == num_str[::-1]:
        print("Palindrome")
    else:
        print("Not a Palindrome")

number = int(input("Enter an integer: "))
is_palindrome(number)