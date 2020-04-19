print("Testing if something is a palindrome")
print("A word or a string is said to be palindrome if reverse of the string is same as that word or that string.")
s = input("Please enter a word or string: ")
s = list(s.lower())
print(s)
while " " in s:
    s.remove(" ")
while "." in s:
    s.remove(".")
while "'" in s:
    s.remove("'")
z = s[::-1]
print()
if s == z:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
