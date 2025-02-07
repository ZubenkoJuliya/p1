n = int(input("Введите высоту прямоугольника (n): "))
m = int(input("Введите ширину прямоугольника (m): "))
symb = input("Введите символ, из которого будет построен прямоугольник: ")

for i in range(n):
    if i == 0 or i == n - 1:
        print(symb * m)
    else:
        print(symb + ' ' * (m - 2) + symb)
