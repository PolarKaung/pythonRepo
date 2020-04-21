a = { 12: 'a', 21: 'b', 2: 'c', 'e': 43}
key = []
value = []

for x,y in a.items():
    key.append(x)
    value.append(a[x])

    
print("key list = ",key)
print("value list = ",value)
