print("Palindrome: Reading words forwards from the beginning or backwards from the end are the same.\n")

a = input("Please write numbers or words or sentences:")
b = a[::-1]
if a == b:
    print(b)
    print("It is palindrome")
else:
    print("it is not a palindrome")
