salary = 1500

camera = int(input("Enter the number of cameras sold:"))
campri = float(input("Enter the prize for cameras:"))

commission = 0.02*camera*campri
bonus = 200*camera

total = salary+commission+bonus
print("Bonus = %7.2f" %bonus)
print("Commission = %7.2f" %commission)
print("Total Salary = %7.2f" %total)



