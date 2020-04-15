salary=1500
bonus=200
commission=0.02
no_of_camera_sold=int(input("Enter the number of cameras sold : "))
total_price=float(input("Enter the total price : "))
total_salary=salary+(bonus*no_of_camera_sold)+(total_price*commission*no_of_camera_sold)
print("total salary of the camera salesman is",total_salary)
