pun = ("!@#$%^&*()<>?")
p = list(pun)

for i in range(len(pun)):
    datas = input("Enter Anything : ")
    data = datas.replace(" ","")
    d = list(data)
    r_data = data[::-1]
    
    if p[i] in d:
        print("The input goes wrong")
        continue
    
    else:
        
        if data == r_data:
            print("Original Data:",data,"\n","Reverse : ",r_data)
            print("It is palindrome")
            break
        else:
            print("It is not palindrome")
            break
            
        
        

    

