x=int(input("Enter Natural positive Number\t"))
y=1
count=0
while y <= x:
    if x % y == 0:
        count += 1
    y+=1

print("The count of this number divisors is\t",count)
