import numpy as np

while True:
    #sticks = [i for i in range(1,22)]z
    sticks = 21
    c = 0
    #print(sticks)
    print("GAME OF STICKS\na person can only choose 1 to 4 sticks at a time.\nthe one who picks the last stick will lose.")
    while True:
        while True:
            while True:
                while True:
                    try:
                        print("\nit is yours turn to choose.")
                        a = int(input("ENTER the number of sticks you chose : "))
                    except ValueError:
                        print("Invalid input! Enter one more time.")
                        continue
                    break
                if a in range(1,5):
                    break
                print("Invalid input! Enter again.")
            c = c + a
            #print("the total sticks chosen = %d"%c)
            if c >= sticks:
                print("you lose.")
                while True:
                    while True:
                        ans = input("\none more try ('y'/'n'):")
                        if ans in ('y','n'):
                            break
                        print("Invalid input! Enter one more time.")
                    if ans == 'y':
                        c = 0
                        break
                    else:
                        print('BYE')
                        quit()
            else:
                break
            
        while True:    
            print("\nit is the computer's turn to choose.")   
            b = np.random.randint(low = 1, high = 4, size = 1)
            print("the number of sticks computer chose = %d "%b)
            c = c + b
            #print("the total sticks chosen = %d"%c)
            if c >= sticks:
                print("you win.")
                while True:
                    while True:
                        ans = input("\none more try ('y'/'n'):")
                        if ans in ('y','n'):
                            break
                        print("Invalid input! Enter one more time.")
                    if ans == 'y':
                        c = 0
                        break
                    else:
                        print('BYE')
                        quit()
                break
            else:
                break
        
        
