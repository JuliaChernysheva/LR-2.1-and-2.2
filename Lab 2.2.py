# Задание 1. Счастливая последовательность 1
print("Задание 1:")
print(4, 8, 15, 16, 23, 42)
print()

# Задание 2. Счастливая последовательность 2
print("Задание 2:")
print(4)
print(8)
print(15)
print(16)
print(23)
print(42)
print()

# Задание 3. Звездный треугольник
print("Задание 3:")
for i in range(1, 8):
    print('*' * i)
print()

# Задание 4. Любимая команда
print("Задание 4:")
team = input("Введите название команды: ")
print(team, "- чемпион!")
print()

# Задание 5. Повторяй за мной
print("Задание 5:")
line1 = input("Введите первую строку: ")
line2 = input("Введите вторую строку: ")
line3 = input("Введите третью строку: ")
print(line3)
print(line2)
print(line1)
print()

# Задание 6. I like Python
print("Задание 6:")
print("I", "like", "Python", sep="***")
print()

# Задание 7. Кастомный разделитель
print("Задание 7:")
separator = input("Введите разделитель: ")
str1 = input("Введите первую строку: ")
str2 = input("Введите вторую строку: ")
str3 = input("Введите третью строку: ")
print(str1, str2, str3, sep=separator)
print()

# Задание 8. Звездный прямоугольник
print("Задание 8:")
print('*' * 17)
for _ in range(2):
    print('*' + ' ' * 15 + '*')
print('*' * 17)