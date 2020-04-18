a=input("Enter the word you want to check : ")
a=list(a.lower())
while " " in a:
    a.remove(" ")
print(a)
a_rev=a[::-1]
print("The reversed word is : ",a_rev)
if a == a_rev :
    print("This word is a palindrome.")
else:
    print("This word is not a palindrome.")
