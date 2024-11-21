#TODO Задание 1
def cordination(x,y):
    if x > 0 and y > 0:
        print('I')
    elif x < 0 and y > 0:
        print('II')
    elif x <0 and y < 0:
        print('III')
    elif x > 0 and y< 0:
        print('IV')

cordination(11,5)

#Todo Задание 2
def ask_pasword():
    password = 'password'
    user_pass = input('Введите пароль:')
    count = 0
    if user_pass != password:
        print('неверный пароль!')
        count += 1
        if user_pass == password:
            print('Пароль принят!')

while True:
    ask_pasword()

