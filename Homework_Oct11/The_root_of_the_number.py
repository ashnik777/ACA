#This is recursive function 

def root(n):
    sum=0
    while n > 0:
        sum += n%10
        n //=10
    if sum <= 10:
        print(sum)
    else:
        print(sum)
        root(sum)

    
x=int(input("Enter Natural Number\t"))
print("***************************")
print(x) 
root(x)
