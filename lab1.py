#1
fileId = int(input('Введите айди из 3х цифр: '))
sumId = 0
mulId = 1

for i in str(fileId):
    sumId += int(i)
    mulId *= int(i)

print(sumId)
print(mulId)

if (sumId % 3 == 0 and mulId % 5 ):
    print('Файл не поврежден')
else:
    print('Файл изменен')

#2
user_password ='user_123'
attempts = 0

flag = True

while flag:
    user_input = input('Введите пароль:')
    if (user_input == user_password):
        print('Вы успешно вошли в систему')
        attempts = 0 
        break
    else:
        attempts += 1
        print('Неверный пароль!\nПопытка:',attempts)
        if (attempts % 3 == 0):
            print('Аккаунт временно заблокирован')


#3

level = int(input('Введите уровень угрозы от 1 до 100: '))
threshold = 60

if (level> threshold):
    print('Превышает порог')
elif (level == threshold):
    print('Равен порогу')
elif (level<= threshold - 20):
    print('Меньше на 20 или более')
else:
    print('Меньше порога')



#4
banned_logins = ['admin','root','superuser']

login = input('Введите логин:')
password = input('Введите пароль:')

has_digit = False
for sym in password:
    if sym in '0123456789':
        has_digit = True
        break

if (login not in banned_logins) and (len(password)>= 8 and has_digit):
    print('Доступ разрешен')
else:
    print('Доступ запрещен')


#5
x = int(input('Введите число: '))

print('x & 1:',x & 1)  
print('x << 1:',x << 1) 
print('x >> 1:',x >> 1) 
print('x | 1:',x | 1)  
print('x ^ 1:',x^1)   

if (x & 1 == 0):
    print('Число четное')
else:
    print('Число нечтное')


a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)  
print(a is b)  
print(a is c)