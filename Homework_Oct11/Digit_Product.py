number=int(input("Enter natural number\t"))
res=1
while number > 0:
    if number % 10 != 0:
        res *= number % 10
    number //= 10

print("Your answer ",res)

