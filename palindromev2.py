
b = '"'
c = "!@#$%^&*()1234567890-=_+<>?/.,:;\|}{][ '"
d = b + c


check = input("enter the string to check : ")
a = check.lower()
a = [a[i] for i in range(len(a))]

e = []
for i in a:
    if i not in d:
        e.append(i)


reverse = e[::-1]
print("the reverse string is ",''.join(reverse[i] for i in range(len(reverse))))
if check == reverse:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


        
