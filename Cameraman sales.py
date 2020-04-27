salary = 1500
number = int(input("Enter the no of cameras sold:"))
price = float(input("Enter total price of the cameras:"))
bonus = (200*number)

commission = (0.02*number*price)
total_bonus = (salary + bonus + commission)

print("Bonus", bonus)
print("Commission", commission)
print("Total Salary", total_bonus)
