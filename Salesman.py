basic_salary = 1500
bonus = 200
commission = 0.02

no_camera = int(input("Enter the number of camera sold : "))
price = float(input("Enter total prices : "))

total_bonus = float(no_camera * bonus)
total_commission = commission * no_camera * price

print("His total bonus : ", total_bonus)
print("His total commision : ", total_commission)
print("His total salary : ", basic_salary + total_bonus + total_commission)


