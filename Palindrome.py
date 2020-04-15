alphabet = tuple(chr(x) for x in range(0x61,0x7b)) #alphabet list

while True:
    sentence = input("Enter the sentence\n").lower()#not to be case sensitive
    final = list(x for x in sentence if x in alphabet)#taking only the alphabet

    count = round(len(final) /2)
  #  print(final,count)
    for i in range(count+1):
        if final[i] is final[-i-1]:
            state = True
        else:
            state = False
            break
    if state is True :
        print("That is a palindrome.")
    else:
        print("That is not a palindrome.")
    again = input("Wanna try again?\n'y' for yes, anything for no :")
    if again == 'y':
        continue
    else:
        break
