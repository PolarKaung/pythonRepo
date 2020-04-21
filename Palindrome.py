print("Testing if something is a palindrome")
print("A word or a string is said to be palindrome if reverse of the string is same as that word or that string.")
s = input("Please enter a word or string: ")
s = s.lower()
# converting ch in string into unicode point of that ch
list = [ord(ch) for ch in s]
z =[]
#sorting out a to z
for num in list:
    if num >= 97 and num <= 122:
        z.append(num)
#palindrome checking
if z == z[::-1]:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
