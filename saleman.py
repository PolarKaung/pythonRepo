basic_salary = 1500
bonus_price = 200
percentage = 0.02

sale = int(input("Enter the number of cameras sold out:"))
price = float(input("Enter the total price of the cameras:"))

monthly_bonus = sale * bonus_price
commission = percentage * price * basic_salary

total_salary = basic_salary + monthly_bonus + commission

print("The total slary of a camera saleman is", total_salary)
