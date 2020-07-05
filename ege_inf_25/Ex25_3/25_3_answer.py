x = int(input())
y = int(input())

if x <= 7 and y >= 3:
    print(x + 1, y - 2)
if x <= 7 and y <= 6:
    print(x + 1, y + 2)
if x <= 6 and y >= 2:
    print(x + 2, y - 1)
if x <= 6 and y <= 7:
    print(x + 2, y + 1)

if x >= 3 and y >= 2:
    print(x - 2, y - 1)
if x >= 3 and y <= 7:
    print(x - 2, y + 1)
if x >= 2 and y >= 3:
    print(x - 1, y - 2)
if x >= 2 and y <= 6:
    print(x - 1, y + 2)
