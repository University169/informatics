a = []
n = int(input())
for i in range(n):
    a.append(int(input()))
maximum = 0
for i in range(n):
    if (a[i] < 1000) and (a[i] > maximum) and (a[i] % 2 == 0):
        maximum = a[i]
num = (1000 // maximum) + 1
if maximum != 0:
    for i in range(n):
        if a[i] % 2 == 0 and a[i] < 1000:
            a[i] *= num
print(a)
