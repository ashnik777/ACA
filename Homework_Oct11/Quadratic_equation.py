import math
a=float(input("Enter a\t"))
b=float(input("Enter b\t"))
c=float(input("Enter c\t"))
print("******************")


def dis(a,b,c):
        d=(b*b)-(4*a*c)
        if d<0:
            print("Discriminant:\t",d)
            print("No Solution")
        elif d == 0:
            print("Discriminant:\t",d)
            print("One solution\t",-b/(2*a))
        else:        
            print("Discriminant:\t",d)
            print("Two solution:\t",(-b-math.sqrt(d))/(2*a),(-b+math.sqrt(d))/(2*a))

if a == 0:
    if b == 0:
        if c == 0:
            print("Non-quadratic equation")
            print("Infinite solution")
        else:
            print("Non-quadratic equation")
            print("No Solution")
    else:
        print("Non-quadratic equation")
        print("One solution\t",-c/b)
else:
    print("Quadratic equation")
    dis(a,b,c)
