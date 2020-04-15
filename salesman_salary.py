
camera_price = float(input("Enter the total price of cameras sold ="))

basic_salary = 1500

sf_s = camera_sold * 200
sf_c = camera_sold * camera_price * 0.02

salary = sf_s + sf_c + basic_salary

print("\nthe total salary is %f"%(salary))
        
