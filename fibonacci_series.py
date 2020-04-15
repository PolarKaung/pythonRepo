#For checking non-negative integer
def nicheck(number):
    state = True
    checknum = 0
    try:
        checknum = int(number)
        if checknum < 0:
            state = False
            print("The number must be non-negative.")
    except ValueError:
        print("The number must be integer.")
        state = False
    return checknum,state


while True:
    while True:
        #First Number
        first_no = input("Enter the First number :")
        first_no,first_state = nicheck(first_no)
        if first_state is False:
            continue
        else:
            break
    while True:
        #Second Number
        second_no = input("Enter the Second number :")
        second_no,second_state = nicheck(second_no)
        if second_state is False:
            continue
        else:
            break
    if first_no > second_no:
        #To ensure that 1st is less than 2nd
        print("Second Number must be larger than First Number.")
        continue
    else:
        break

while True:
    #Sequence Count
    times = input("How many more numbers would you like to produce? :")
    times,times_state = nicheck(times)
    if times_state is False:
        continue
    else:
        break
original = [first_no,second_no,times + 2]
sequence = [first_no,second_no]

while times >0 :
    third_no = first_no + second_no
    sequence.append(third_no)
    first_no,second_no = second_no,third_no
    times -= 1

print("The Fibonnaci starts with {} and ends with {} to {} time is".format(*original))
print(sequence)
