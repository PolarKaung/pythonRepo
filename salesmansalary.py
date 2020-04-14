basic_salary = 1500
c = int(input("Enter the no of cameras sold:"))
p = float(input("Enter total price of the cameras:"))
bonus = (200*c)
commission = (0.02*c*p)
total_salary = (basic_salary + bonus + commission)
print("Bonus", bonus)
print("Commission", commission)
print("Total Salary", total_salary)
