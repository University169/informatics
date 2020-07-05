# Оптимальное решение

n = int(input())
d = 4
nk = [0] * d
kr = [0] * d
k = 0
for i in range(1, n+1):
    x = int(input())
    if x % 3 == 0:
        if i >= (d+1):
            k += nk[i % d]
        kr[i % d] = kr[(i-1) % d] + 1
        nk[i % d] = nk[(i-1) % d]
    else:
        if i >= (d+1):
            k += kr[i % d]
        nk[i % d] = nk[(i-1) % d] + 1
        kr[i % d] = kr[(i-1) % d]
print(k)
