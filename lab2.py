#1

password = input('Введите пароль: ')

if (len(password) < 8):
    print("Слишком короткий пароль")
if (len(password) >= 8):
    print('Пароль принят')

#2

status = 'online'

if (status == 'online'):
    print('Связь установлена')
else:
    print('Связь потеряна')


#3
danger_level = int(input('Введите уровень угрозы(1-100): '))

if (danger_level >= 1 and danger_level < 30):
    print('Низкий уровень угрозы')
elif (danger_level >= 31 and danger_level < 70):
    print('Средний уровень угрозы')
elif (danger_level >= 71 and danger_level < 100):
    print('Критический уровень угрозы')
else:
    print('Ошибка ввода')


#4
checksum_original = input()
checksum_current = input()

status = "Файл не изменён" if checksum_current == checksum_original else "Файл повреждён"
print(status)

#5
event_code = input('Введите тип события: ')

match event_code:
    case 'ERR':
        print("Ошибка системы")
    case 'WRN':
        print("Предупреждение")
    case 'INF':
        print("Информационное сообщение")
    case _:
        print('Неизвестный код события')
