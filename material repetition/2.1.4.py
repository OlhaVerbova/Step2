def return_num_word(text):
    sum_word = None
    text_list = []
    text_list = text.split()
    sum_word = len(text_list)
    return sum_word

text = input()
print(return_num_word(text))