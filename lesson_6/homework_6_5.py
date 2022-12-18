# ** 5. Реализовать функцию, возвращающую n шуток, сформированных из трех случайных слов,
# взятых из трёх списков(по одному из каждого)
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра",
#            "позавчера", "ночью", "когда-то", "где-то"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
# in
# 10 True
# out
# ['дом ночью мягкий', 'огонь завтра зеленый', 'лес вчера яркий',
#     'автомобиль сегодня веселый', 'город позавчера утопичный']
# in
# 10 False
# ['автомобиль ночью мягкий', 'огонь вчера веселый', 'автомобиль позавчера веселый',
#  'город вчера утопичный', 'лес сегодня зеленый', 'дом вчера яркий', 'автомобиль вчера зеленый',
#  'огонь позавчера яркий', 'огонь где-то утопичный', 'автомобиль где-то мягкий']

from random import randint


def gen_joke(some_list):
    short_string = some_list[randint(0, (len(some_list) - 1))]
    return short_string


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра",
           "позавчера", "ночью", "когда-то", "где-то"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

n = int(input('Укажите количество шуток, сформированных из трех случайных слов: '))

joke_list_true = [
    f'{gen_joke(nouns)} {gen_joke(adverbs)} {gen_joke(adjectives)}']
joke_list_false = []

for ind in range(1, n):
    joke_string = f'{gen_joke(nouns)} {gen_joke(adverbs)} {gen_joke(adjectives)}'
    counter = 0
    for elem in joke_list_true:
        if joke_string.split()[0] == elem.split()[0]:
            counter += 1
    if counter == 0:
        joke_list_true.append(joke_string)
    else:
        joke_list_false.append(joke_string)

print(f'{(" " * 5)} Из {n} - True')
joke_count = 1
for joke_elem in joke_list_true:
    print(f'{joke_count}. {joke_elem}')
    joke_count += 1

print(f'{(" " * 5)} Из {n} - False')
for joke_elem in joke_list_false:
    print(f'{joke_count}. {joke_elem}')
    joke_count += 1
