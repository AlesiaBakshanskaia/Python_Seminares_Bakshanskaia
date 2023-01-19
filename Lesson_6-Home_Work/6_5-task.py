# 5. Реализовать функцию, возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого)
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "когда-то", "где-то"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
from random import choice, shuffle
import sys
def make_joke(num, truth_false):
    jokes = []
    if truth_false:
        nouns2 = nouns.copy()
        shuffle(nouns2)
        adverbs2 = adverbs.copy()
        shuffle(adverbs2)
        adjectives2 = adjectives.copy()
        shuffle(adjectives2)

        while len(nouns2) > 0 and len(adverbs2) > 0 and len(adjectives2) > 0:
            joke = f'{nouns2.pop(0)} {adverbs2.pop(0)} {adjectives2.pop(0)}'
            jokes.append(joke)
        

    
    
    else:
        for i in range(num):
            rand_nouns, rand_dverbs, rand_adjectives = \
                choice(nouns), choice(adverbs), choice(adjectives)
            joke = f'{rand_nouns} {rand_dverbs} {rand_adjectives}'
            jokes.append(joke)
    print(jokes)

num_joke = int(input('Введите количество шуток: '))
if num_joke < 1:
    print("Вы ввели не верное значение")
    sys.exit()

TF = input('Введите True или False: ')
if TF == 'True':
    TF = True
elif TF == 'False':
    TF = False
else: 
    print("Вы ввели не верное значение")
    sys.exit()


make_joke(num_joke, TF)