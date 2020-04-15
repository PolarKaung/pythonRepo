a = int(input("Enter the number of cameras sold: "))
b = float(input("Enter the total price of all the cameras: "))

#basic salary
bs = 1500

#bonus
bonus = a*200

#commission
c = b*0.02

net_salary = bs + bonus + c

print("The net salary of the camera salesman is: ", net_salary)
