n = int(input())
d = 4
nk = [0] * d
kr = [0] * d
for i in range(1, d):
    x = int(input())
    if x % 3 == 0:
        kr[i] += kr[i-1] + 1
        nk[i] += nk[i-1]
    else:
        nk[i] += nk[i-1] + 1
        kr[i] += kr[i-1]
x = int(input())
if x % 3 == 0:
    kr[0] += kr[d] + 1
    nk[0] += nk[d]
else:
    nk[0] += nk[d] + 1
    kr[0] += kr[d]
# получили kr и nk - количество кратных и некратных к i%d моменту
k = 0
for i in range(d+1, n+1):
    x = int(input())
    if x % 3 == 0:
        k += nk[i % d]
        kr[i % d] = kr[(i-1) % d] + 1
        nk[i % d] = nk[(i-1) % d]
    else:
        k += kr[i % d]
        nk[i % d] = nk[(i-1) % d] + 1
        kr[i % d] = kr[(i-1) % d]
print(k)