bs = 1500 

qty = int(input("How Much Camera did he sell? -")) 
price = int(input("What is the total price of the cameras? -"))

#bs is basic salary, qty is quantities of camera
salary = bs + (200*qty) + (price*0.02)

print("The total salary of the camera man is",salary)
