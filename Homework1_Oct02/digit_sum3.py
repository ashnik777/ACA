num=int(input("Enter a number\t"))
res=0
while num>0:
    res+=num%10
    num=num//10
print("your sum of digits =",res)
