A = input("enter anything you want")
A = list(A)

length = len(A)

count = 0
for i in range(length):
     if A[i]==A[length-i-1]:
        count+=1

if count==length:
    print("\t Given input is palindrome")
else:
    print("\t Given input is not paliondrome")
