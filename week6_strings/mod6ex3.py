def loop():
    word = input('Enter a fruit: ')
    letter = input('What letter are you looking for: ')
    count = 0
    for l in word:
        if l == letter:
            count = count + 1
    print(count)
loop()
