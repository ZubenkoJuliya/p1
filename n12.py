N = int(input("Введите целое положительное число N: "))
n1 = 1

for i in range(1, N + 1):
    numbers = []
    for j in range(i):
        if n1 <= N:
            numbers.append(str(n1))
            n1 += 1
    print(' '.join(numbers))
