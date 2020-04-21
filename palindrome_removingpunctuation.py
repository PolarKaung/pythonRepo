print("Palindrome: Reading words forwards from the beginning or backwards from the end are the same.\n")

a = input("Please write numbers or words or sentences:")
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

b = b1 = ""
for i in a :
    if i in punctuations:
        b += i
    else:
        b1 += i
print("punctuations in the written sentence:\n" , b)
print("after removing punctuations:\n" , b1)

c = b1[::-1]
if c == b1:
    print("reverse of the written sentence:\n", c)
    print("It is palindrome.")
else:
    print("It is not a palindrome.")
