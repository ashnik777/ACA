a=int(input("Enter first side\t"))
b=int(input("Enter second side\t"))
c=int(input("Enter thirth side\t"))
print("***************************")
if a+b > c and a+c > b and b+c > a:
    if a >= b and a >= c:
        angle = (b**2 + c**2 - a**2) / 2*b*c
    elif b >= a and b >= c:
        angle = (a**2 + c**2 - b**2) / 2*a*c
    elif c >= a and c >= b:
       angle = (a**2 + b**2 - c**2) / 2*a*b

    if angle > 0:
        print("Acute Triangle")
    elif angle == 0:
        print("Right Triangle")
    elif angle < 0:
        print("Obtuse Triangle")
else:
    print("NO Triangle")
