a=input("Enter the word you want to check : ")
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
b = ""
for char in a:
   if char not in punctuations:
       b+=char
b=list(b.lower())

while " " in b:
    b.remove(" ")

print(b)
b_rev=b[::-1]
print("The reversed word is : ",b_rev)
if b == b_rev :
    print("This word is a palindrome.")
else:
    print("This word is not a palindrome.")
