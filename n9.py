while True:
    password = input("Введите пароль: ")
    password2 = input("Подтвердите пароль: ")

    if len(password) < 8:
        print("Короткий!")
    elif "123" in password:
        print("Простой!")
    elif password != password2:
        print("Различаются.")
    else:
        print("OK")
        break
