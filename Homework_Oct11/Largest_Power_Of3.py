x=int(input("Enter Natural number \t"))
b=1
k=1
while b <= x/3:
    k += 1
    b = 3**k
print(b)
