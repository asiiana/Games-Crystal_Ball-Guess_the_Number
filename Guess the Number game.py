import random

print('Добро пожаловать в игру "Угадай число"!')

def is_valid(n):
    return n.isdigit() and int(n) in range(1, int(range_end) + 1)

want_play = True

while want_play:
    range_end = input('Укажите правую границу диапазона, в котором Вы хотите угадывать числа, - от 1 до: ')
    while not (range_end.isdigit() or int(range_end) > 0):
        print('Необходимо ввести целое число больше 0')
        
    num = random.randint(1, int(range_end))
    print(num)
    tries = 0
    guessed = False

    while not guessed:
        n = input(f'Введите число от 1 до {range_end}: ')
        tries += 1
        
        if not is_valid(n):
            print(random.choice([f'Чтобы продолжить игру, нужно ввести целое число от 1 до {range_end}', f'Необходимо ввести целое число от 1 до {range_end}. Попробуйте еще раз!']))
            continue
        
        n = int(n)    
        if n != num:
            if n < num:
                print('Ваше число меньше загаданного, попробуйте еще разок')      
            elif n > num:
                print('Ваше число больше загаданного, попробуйте еще разок')            
            
        else:
            guessed = True
            print(f'Вы угадали c {tries} раза, поздравляем!')
            if input('Если хотите сыграть еще раз, просто нажмите пробел: ') == ' ':
                want_play = True
            else:
                print('Спасибо, что играли в игру "Угадай число". Еще увидимся...')
                want_play = False
            break