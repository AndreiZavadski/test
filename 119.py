import random

num_1 = int(input('Введите большое число :'))
num_2 = int(input('Введите маленькое число :'))

comp_num = random.randint(num_2, num_1)

print('I am thinking of a number... ')
num_3 = int(input('Попробуйте угадать загаданное число : '))

if comp_num == num_3:
    print('Correct, you win')
elif comp_num > num_3:
    print('Данное число меньше загаданного ')
    num_3 = int(input('Попробуйте угадать загаданное число : '))
    if comp_num == num_3:
        print('Correct, you win')
    else:
        num_3 = int(input('Попробуйте угадать загаданное число : '))
elif comp_num < num_3:
    print('Данное число больше загаданного')
    num_3 = int(input('Попробуйте угадать загаданное число : '))
    if comp_num == num_3:
        print('Correct, you win')
    else:
        num_3 = int(input('Попробуйте угадать загаданное число : '))

