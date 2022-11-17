import pymorphy2

lst = ['политикой', 'ривет', 'ответственного', 'разглашения',  'Обратная связь']
threshold = 0.75

morph = pymorphy2.MorphAnalyzer()

for word in lst:
    p = morph.parse(word)
    score = p[0].score
    print(f'{word} - {"True" if score >= threshold else "False"}')
