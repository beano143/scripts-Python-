import string # if you need more and can't figure it out, get off my page.

all_characters = string.ascii_letters + string.digits + string.punctuation

with open('words_longform.txt', 'a') as file:
    for char1 in all_characters:
        for char2 in all_characters:
            for char3 in all_characters:
                for char4 in all_characters:
                    for char5 in all_characters:
                        for char6 in all_characters:
                            combo = char1 + char2 + char3 + char4 + char5 + char6
                            file.write(combo + '\n')
