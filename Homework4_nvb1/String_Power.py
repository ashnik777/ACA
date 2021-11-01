s = input()
k = int(input())

res = ""
if k >= 0:
    while k>0:
        res += s
        k-=1
    print(res)
else:
    #xyz xyz xyz
        if len(s)%k == 0:   
            res = s[:len(s)//-k]
            if res == s[(len(s)//k):]:
                print(res)
            else:
                print("undifined")
        else:
            print("undifined")



