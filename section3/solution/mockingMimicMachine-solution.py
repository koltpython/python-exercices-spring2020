num = int(input("How many words do you want me to process? "))
words = []
converted_words = []
vowels = ['a', 'e', 'ı', 'i', 'o', 'ö', 'u', 'ü']

for i in range(num):
    inp = input(f'What is word #{i+1}? ')
    words.append(inp)

for word in words:
    new_word = ''
    for i in range(len(word)):
        if word[i] in vowels:
            new_word += 'o'
        else:
            new_word += word[i]
    converted_words.append(new_word)

print(converted_words)
