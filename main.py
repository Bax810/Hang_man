import random

categories = ['Страны', 'Аниме', 'Игры']
words = [
    ['Россия', 'Уругвай', 'Нигерия'],
    ['Атака титанов', 'Наруто', 'Ван Пис'],
    ['Ведьмак', 'Киберпанк', 'Скайрим'],

]


def sad_man(suisaid):
    if suisaid == 1:
        print('''
          +---+
          |   |
              |
              |
              |
              |
        =========''')

    elif suisaid == 2:
        print('''  
          +---+
          |   |
          O   |
              |
              |
              |
        =========''')
    elif suisaid == 3:
        print(''' 
          +---+
          |   |
          O   |
          |   |
              |
              |
        =========''')
    elif suisaid == 4:
        print('''
          +---+
          |   |
          O   |
         /|   |
              |
              |
        =========''')
    elif suisaid == 5:
        print(r''' 
          +---+
          |   |
          O   |
         /|\  |
              |
              |
        =========''')
    elif suisaid == 6:
        print(r'''
          +---+
          |   |
          O   |
         /|\  |
         /    |
              |
        =========''')
    elif suisaid == 7:
        print(r'''
          +---+
          |   |
          O   |
         /|\  |
         / \  |
              |
        =========''')


def start_game():
    for category in categories:
        print(category)
    print('Случайная категория  \n')
    while True:
        choise = input('Введите название категории:').lower()
        lower_categories = list(map(lambda x: x.lower(), categories)) + ['случайная категория']
        if choise in lower_categories:
            break
        else:
            print('Попробуй ввести еще раз ')

    choise = choise.capitalize()
    return choise


def find_category_index(name_category):
    for index in range(0, len(categories)):
        if categories[index] == name_category:
            return index
    return random.randrange(0, len(categories))


def game(word):
    pole = gen_pole(word)
    error = 0
    all_words = []
    while True:
        sad_man(error)
        norm_pole(pole)
        win = check_win(pole)
        if win:
            print('Победа,ваш айкью равен 20')
            break
        if error == 7:
            print('Ваш айкью меньше нуля ')
            print(word)
            break
        while True:

            print('Вы вводили:', *all_words)
            x = input('Введите букву:').lower()
            if x in all_words:
                print('ты вводил уже эту букву алло')
            else:
                break

        all_words.append(x)
        error += check_letter(word, x, pole)


def check_win(pole):
    if '_' in pole:
        return False
    return True


def check_letter(word, x, pole):
    num = 0
    for index, y in enumerate(word):
        if x == y.lower():
            pole[index] = word[index]
            num += 1
    return 1 if num == 0 else 0


def gen_pole(word):
    pole = []
    for s in word:
        if s == ' ':
            pole.append(' ')
        else:
            pole.append('_')
    return pole


def norm_pole(pole):
    for h in pole:
        print(f'{h}  ', end='')
    print()


name_category = start_game()
index_category = find_category_index(name_category)
word = random.choice(words[index_category])
game(word)
