a = input("Enter a string: ")
a = a.lower() #change to small letter

v = [c for c in a] #change into the form of list


B = [] #To remove comma br nyr
F= [] #To change into char
output = [] #To check palindrome 

A = [ord(c) for c in a] #ASCII Code 

for i in range(len(v)):
    if(97 <= A[i] <= 122):
        B.append(A[i])
print(B)
b = len(B)
print(b)

for i in range(b):
    ch = chr(B[i])
    F.append(ch)
print(F)

f = len(F)

for b in range(f):
    output.append(F[-b-1])
print(output)

compare = F == output
if compare == True:
    print("The given is a palimdrone")
else:
    print("The given is not a palimdrone")

