n = 30
a = []
for i in range(n):
    num = int(input())
    a.append(num)
even_counter = 0
maximum = 0
for i in range(n):
    if a[i] % 2 == 0:
        even_counter += 1
        if even_counter > maximum:
            maximum = even_counter
    else:
        even_counter = 0
print(maximum)
