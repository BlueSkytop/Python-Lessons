# Вивести кожне число зі списку

numbers = [1, 2, 3, 4, 5]

print(len(numbers))
for item in numbers:
    print(item)
print('-------------')

# Створи масив із 10 будь-яких чисел. За допомогою циклу підрахуй, скільки серед них парних чисел.
arrNumbers = [27, 56, 12, 2, 88, 67, 10, 8, 11, 55]
counter = 0
for num in arrNumbers:
    if num % 2 == 0:
        counter = counter + 1
print(counter)
print('-------------')

# Створи масив із 5 чисел. За допомогою циклу порахуй суму всіх чисел у цьому масиві.
list = [45, 8, 7, 48, 13]
total = 0
for x in list:
    total = total + x
print(total)
print('-------------')

# Є об’єкт (словник), у якому зберігаються імена студентів та їхніх пропусків.
# За допомогою циклу виведи на екран усіх студентів у такому форматі:
# Ім'я: Петро, Пропусків: 18
#students = {
#    "Петро": 18,
#    "Оля": 20,
#    "Іван": 17
#}
#
#for student in students:
#    print(f"Ім'я: {student}, Пропусків: {students[student]}")
students = {
    'Олег': 5,
    'Катерина': 3,
    'Іванка': 6,
    'Ілона': 0,
    'Максим':5
}
for student in students:
    print(f"Ім'я: {student}, Пропусків: {students[student]}")