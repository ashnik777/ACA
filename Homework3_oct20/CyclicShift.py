num = int(input("Enter the length of sequence: "))
l = int(input("Enter the count of shifts: "))

if k >= num:
    k -= num*(k//num)

seq = []
for i in range(num):
    seq.append(int(input()))

seq = seq[num-k:] + seq[:num-k]
print(seq)
