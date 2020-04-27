n = int(input("Enter the counts of data : "))
my_dict = dict()
for i in range(n):
    data= input("Enter keys and values sparated by ':' ")
    key,value = data.split(":")
    my_dict[key] = value

print("Dictionary List : \n",my_dict)

key =[]
value = []
for x in my_dict:
    key.append(x)
for y in my_dict.values():
    value.append(y)

print("Key List : \n",key)
print("Value List : \n",value)
