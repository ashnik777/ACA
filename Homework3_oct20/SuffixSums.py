n = int(input("Enter count of elements in sequence: "))

seqa = []
for i in range(n):
    seqa.append(float(input()))

seqb = []
for i in range(n):
    seqb.append(sum(seqa[i:]))

print(seqb)
