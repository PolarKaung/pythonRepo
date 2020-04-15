while True:
    while True:
        try:
            camno = int(input("Enter the number of camera sold :"))
            if camno < 0 :
                print("The number must be non-negative.")
                continue            
        except ValueError:
            print("The number must be integer.")
            continue
        else:
            break
    while True:
        try:
            camprice = float(input("Enter the price of a camera :"))
            if camprice < 0 :
              print("The Price must be non-negative.")
              continue
        except ValueError:
            print("The number must be float or integer.")
            continue
        else:
            break

    salary = 1500 + (200 * camno) + (camno * camprice * 0.02)
    print(f"His total salary is ${salary:.2f}")
    while True :
        quit = input("Would you like to calculate again?\nType 'y' to do again or type 'q' to exit :")
        if quit == "y" or quit == "q":
            break
        else:
            print("Please Enter the correct command")
    if quit == "q":
        break
    else:
        continue
print("Thanks for using me.")    
