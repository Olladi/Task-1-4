#Задание 1. Круговой массив
n, m = map(int, input().split())
i = 1
while True:
    print(i, sep='', end = '')
    i = 1 + (i + m - 2) % n
    if i == 1:
        break
print()
