list = [54,26,93,17,77,31,44,55,20]

def bubblesort(list):
    s = len(list) - 1
    for i in range(s,0,-1):
        for j in range(i):
            k = j+1
            if list[j]>list[k]:
                temp = list[j]
                list[j] = list[k]
                list[k] = temp

bubblesort(list)
print("Bubble sort:", list)

def b_search (list, n):
    start = 0
    stop = len(list) - 1
    
    while start <= stop:
        midpoint = start + (stop - start) // 2
        midpoint_value = list[midpoint]
        if midpoint_value == n :
            return midpoint

        elif n < midpoint_value:
            stop =  midpoint - 1

        else:
            start = midpoint + 1

    return -1

list1 = list
a = int(input("Please enter the number in the above list:"))
result = b_search (list1, a)

if result != -1: 
    print ("index = % d" % result) 
else: 
    print ("It is not present in the above list.") 


