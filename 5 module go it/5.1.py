"""Напишіть функцію real_len, яка підраховує та повертає
довжину рядка без наступних керівних символів: [\n, \f, \r, \t, \v]

Для перевірки правильності роботи функції real_len їй будуть передані наступні рядки:
#["\n", "\f", "\r", "\t", "\v"]
'Alex\nKdfe23\t\f\v.\r'
'Al\nKdfe23\t\v.\r'"""
def real_len(text):
    no_calculate = ["\n", "\f", "\r", "\t", "\v"]
    sum = 0
    for char in text:
        if char not in no_calculate:
            sum += 1
    return sum


text = input("Enter Text: ")
print(real_len(text))