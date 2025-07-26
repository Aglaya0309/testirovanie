def count_russian_vowels(text):

    russian_vowels = {'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я'}
    count = 0
    for char in text.lower():
        if char in russian_vowels:
            count += 1
    return count