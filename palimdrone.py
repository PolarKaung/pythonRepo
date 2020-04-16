A = [input("Enter a senstence or a word to check: ")]
output = []

B = []
D = []
B[:0] = A[0]

print("The original word: ",B)

for i in range(len(B)):
    if " " in B:
        B.remove(" ")
print(B)
C = len(B) 
    
for b in range(C):
    output.append(B[-b-1])
print("The change of order: ",output)

compare = B == output
if compare == True:
    print("The given is a palimdrone")
else:
    print("The given is not a palimdrone")
