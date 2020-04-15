while True:
    nterms = int(input("How many terms? "))

    n1, n2 = 0, 1
    count = 0

    while True:
        if nterms <= 0:
           nterms = int(input("Please enter the positive integer :"))
        else:
           print("Fibonacci sequence:")
           while count < nterms:
               print(n1)
               nth = n1 + n2
               # update values
               n1 = n2
               n2 = nth
               count += 1
        break
