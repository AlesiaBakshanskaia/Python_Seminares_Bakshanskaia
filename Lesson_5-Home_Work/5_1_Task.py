# Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
from random import sample

def create_text(num: int, collect: str='абв'):
    list_words = []
    for i in range(num):
        word = sample(collect, k=3)
        list_words.append("".join(word))
    text = " ".join(list_words)
    return text
num = int(input("Введите количество слов в тексте: "))
import sys
if num < 1:
    print("Вы ввели некорректные данные")
    sys.exit()
our_text = create_text(num)


print(our_text)

result_text = " ".join(list(filter(lambda word: word != 'абв', our_text.split(" "))))
print(result_text)