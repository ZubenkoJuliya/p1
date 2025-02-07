n = input();

if len(n) == 3 and n.isdigit():
    if (s := sum(map(int, n)) / 2) == max(map(int, n)):
        print("Вы ввели красивое число")
    else:
        print("Жаль, вы ввели обычное число")
else:
    print("Ошибка: введите трехзначное число.")
