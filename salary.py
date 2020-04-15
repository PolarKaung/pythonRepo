print("This is a program for calculating monthly salary of camera salesman.")
print("Basic salary is $1500.")
print("Bonus for every camera sold is $200.")
print("Commission rate is 2% monthly.")

base_wage = 1500
bonus = 200 # for each camera sold
com_rate = 0.02 # commission rate
cam = int(input("Please Enter the number of camera sold:"))
tot_amount = int(input("Enter the total price of camera sold:"))
print("The total sales of the camera is $",tot_amount)
grosspay = base_wage + (tot_amount * com_rate)
tot_bonus = bonus * cam
salary = grosspay + tot_bonus
print(" Monthly salary for salesman is $",salary)
