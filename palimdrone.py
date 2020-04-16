A = [input("Enter a senstence or a word to check: ")]
output = []

B = []
B[:0] = A[0] #to change string to char in the list

print("The original word: ",B)

#to remove space if needed

for i in range(len(B)):
    if " " in B:
        B.remove(" ") 
print(B)
C = len(B) 

#to reverse the input (space_removed)

for b in range(C):
    output.append(B[-b-1])
print("The change of order: ",output)

#to check if they are the same

compare = B == output
if compare == True:
    print("The given is a palimdrone")
else:
    print("The given is not a palimdrone")
