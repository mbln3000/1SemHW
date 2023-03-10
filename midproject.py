text = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух... там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""
text = text.lower()
marks = '''!()-[]{};?@#$%:'"\,./^&;*_—'''
for i in marks:
    text = text.replace(i, "")
text = text.replace('\n', " ")
word_list = text.split()
vowels = ['а', 'о', 'э', 'я', 'и', 'у', 'ю', 'ы', 'е', 'ё']

# 1. Вывести слова, у которых только один слог
count = 0
v_count = 0
for j in word_list:
    for w in j:
        for v in vowels:
            if w == v:
                v_count += 1
    if v_count == 1:
        count += 1
    v_count = 0
print(f'Количество слов с одним слогом: {count}')

# 2. Список слов, у которых только две гласных
l = []
for j in word_list:
    for w in j:
        for v in vowels:
            if w == v:
                v_count += 1
    if v_count == 2:
        l.append(j)
    v_count = 0
print(f'Список слов с 2 гласными: {l}')

# 3. Слово, которое встречается наибольшее количество раз, но длиннее 5 символов
l2 = []
l3 = []
d = {}
count = 0
for j in word_list:
    if len(j) > 5:
        l2.append(j)
for c in l2:
    count_c = l2.count(c)
    d[c] = count_c
max_val = max(d.values())
final_dict = {k:v for k, v in d.items() if v == max_val}
for key in final_dict.keys():
    l3.append(key)
print(f"Самые частотные длинные слова: {(', '.join(l3))}")

# 4.  Слова, которые заканчиваются на -ит
import re
result = re.findall(r'[а-я]*ит\s', text)
result = "".join(result)
print(f"Слова на -ит: {result.replace(' ', ', ')}")

# 5. Найти количество предложений и самое длинное предложение
text1 = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух... там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""
import re
text1 = text1.lower()
text1 = text1.replace('\n'," ")
text1 = text1.lstrip()
text1 = text1.rstrip()
sent = re.split(r'(?<=\w[.!?])\s', text1)
print(f"Количество предложений: {len(sent)}")
max_words = 0
for i in sent:
    if len(i.split()) > max_words:
        max_sent = i
        max_words = len(i.split())
print(f'Самое длинное предложение: "{max_sent.capitalize()}"')
