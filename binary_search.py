def LowToHigh(A):
    for j in range(len(A)-1):
        for i in range(len(A)-1):
      
            if A[i] >= A[i+1]:
                put = A[i]
                A[i] = A[i+1]
                A[i+1] = put
    print(A)
    return A


count = 1
A = []
print("Enter s to stop adding number...")
while True:
    a = input("Enter the input %d: "%count)     # In order to type "s", int ko out yout mha pygg ml
    if a == 's':
        break
    else:
        a = int(a)      
        A.append(a)
        count += 1
        
A = set(A)              # to remove same number
A = list(A)             # pee tot list pyan pygg tr :3

B = len(A)
num = int(input("Please type the number to search for: "))


LowToHigh(A)

if num == A[-1]:
    print(num,"is at index %d"%(B-1))
    
l = 0       #lower
u = B-1     #upper

while l<= u:
    
    mid = (l+u)//2
    if num == A[mid]:
        print(num,"is at index %d"%mid)
        break
    elif num < A[mid]:
        u = mid
        mid = (l+u)//2
        if num == A[mid]:
            print(num,"is at index %d"%mid)
            break
    elif num > A[mid]:
        l = mid
        mid = (l+u)//2
        if num == A[mid]:
            print(num,"is at index %d"%mid)
            break
   
  
