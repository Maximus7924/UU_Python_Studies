
def single_root_words(root_word, *other_words):
    root_word_l = root_word.lower()
    same_words = []
    for i in other_words:
        j = i.lower()
        if j.find(root_word_l) != -1:
            same_words.append(i)
        elif root_word_l.find(j) != -1:
            same_words.append(i)
        else:
            continue
    print(f'{root_word} - {other_words} \n {same_words}')


result0 = single_root_words('Bada', 'badass', 'Bad', 'Badarock', 'bugs', 'others')
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
