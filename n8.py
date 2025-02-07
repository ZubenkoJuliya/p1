count = 0
min_height = float('inf')
max_height = float('-inf')

while True:
    height_input = input("Введите рост претендента (или '!' для завершения): ")
    if height_input == "!":
        break
    height = int(height_input)

    if 150 <= height <= 190:
        count += 1
        if height < min_height:
            min_height = height
        if height > max_height:
            max_height = height

if count > 0:
    print("Количество подходящих кандидатов:", count)
    print("Минимальный рост:", min_height)
    print("Максимальный рост:", max_height)
else:
    print("Нет подходящих кандидатов.")
