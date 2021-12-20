import random

answers = ["Бесспорно", "Предрешено", "Никаких сомнений", "Определённо да","Можешь быть уверен в этом", "Мне кажется - да", "Вероятнее всего", "Хорошие перспективы", "Знаки говорят - да", "Да", "Пока неясно, попробуй снова", "Спроси позже", "Лучше не рассказывать", "Сейчас нельзя предсказать", "Сконцентрируйся и спроси опять", "Даже не думай", "Мой ответ - нет", "По моим данным - нет", "Перспективы не очень хорошие", "Весьма сомнительно"]

print('Привет! Я магический шар, и я знаю ответ на любой Ваш вопрос.')
name = input('Напишите свое имя: ')
print(f'Добро пожаловать, {name}!' + '\n')

want_play = ' '
while want_play == ' ':
    print('Ответ на какой вопрос Вы хотели бы узнать?')
    question = input()
    print('Шар сейчас хорошо подумает (но это не точно) и ответит.', 'Ответ магического шара такой:', random.choice(answers).upper(), sep='\n')
    want_play = input('Если у Вас есть еще вопросы, нажмите пробел.')
    
else:
    print('Возвращайтесь, если возникнут еще вопросы!')