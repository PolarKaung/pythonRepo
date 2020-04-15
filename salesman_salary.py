#to calculate the salary of a camera salesman.
#basic salary is 1500,
#for every camera he will sell
#he will get 200 and
#the commission on the month’s sale is 2 %.
#The input will be number of cameras sold and total price of the cameras.


camera_sold = int(input("Enter the number of cameras sold = "))
camera_price = float(input("Enter the total price of cameras sold ="))

basic_salary = 1500

sf_s = camera_sold * 200
sf_c = camera_sold * camera_price * 0.02

salary = sf_s + sf_c + basic_salary

print("\nthe total salary is %f"%(salary))
        
