def bubble_sort(a):
    for x in range (len(a)):
        for y in range (len(a)-1):
            if a[y] > a[y+1]:
                a[y],a[y+1]=a[y+1],a[y]
                

b = []
size = int(input("Enter size of the list:"))
 
for i in range(size):
    numbers = int(input("Enter the number:"))
    b.append(numbers)
print("The list is ",b)
bubble_sort(b)
print("The sorted list is ",b)

c=int(input("Enter the number you want to search :"))
first = 0
last = size-1
find=False
while (first <= last and not find):
    mid= first+(last-first)//2
    if b[mid] < c:
        first=mid+1
    if b[mid] > c:
        last=mid-1
    if b[mid] == c:
        find=True
print("The number is at position ", mid)
    
