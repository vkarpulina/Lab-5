import re
import csv

with open('task1-ru.txt', 'r', encoding='utf-8') as file:
    text = file.read()

capitalized_words = re.findall(r'\b[A-ZА-Я][a-zа-я]*\b', text)
print("Слова, начинающиеся с большой буквы:", capitalized_words)

words_with_colon = re.findall(r'\b\w+\b:', text)
print("Слова, после которых стоит двоеточие:", words_with_colon)

with open('task2.html', 'r', encoding='utf-8') as file:
    html_text = file.read()

closing_tags = re.findall(r'</([a-zA-Z0-9]+)>', html_text)
unique_closing_tags = set(closing_tags)
print("Уникальные закрывающие теги:", unique_closing_tags)

with open('task3.txt', 'r', encoding='utf-8') as file:
    text = file.read()

ids = re.findall(r'\d+', text)
surnames = re.findall(r'[А-Яа-я]+', text)
emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
dates = re.findall(r'\d{2}\.\d{2}\.\d{4}', text)
websites = re.findall(r'https?://[a-zA-Z0-9.-]+', text)

max_len = max(len(ids), len(surnames), len(emails), len(dates), len(websites))

ids.extend([''] * (max_len - len(ids)))
surnames.extend([''] * (max_len - len(surnames)))
emails.extend([''] * (max_len - len(emails)))
dates.extend([''] * (max_len - len(dates)))
websites.extend([''] * (max_len - len(websites)))

data = []
for i in range(max_len):
    data.append([ids[i], surnames[i], emails[i], dates[i], websites[i]])

with open('task3.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['ID', 'Фамилия', 'Электронная почта', 'Дата регистрации', 'Сайт'])
    writer.writerows(data)

print("Данные сохранены в файл task3.csv")
