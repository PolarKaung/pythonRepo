months = ("Jan","Feb","March","April","May","June","July","Aug","Sep","Oct","Nov","Dec")
bs = 1500
ts = 0
for x in months:
    no = int(input("Enter the number of cameras you sold in this month:"))
    ts += ((200 * no + bs) * 0.02) + bs
print("The total salary of this year :", int(ts) ,"Dollars")

