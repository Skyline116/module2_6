def single_root_words(root_word, *other_words):
    same_words = []
    root_word = str(root_word).lower()
    for i in other_words:
        i = str(i).lower()
        if i in root_word:
             same_words.append(i)
        elif root_word in i:
            same_words.append(i)
    print(same_words)


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)