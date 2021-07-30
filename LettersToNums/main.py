letter_num_dict = {
    "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6,
    "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12,
    "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18,
    "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24,
    "y": 25, "z": 26
}

print("Welcome")


def display_text_num_values(text):
    formatted_text = " ".join(text.split())  # removes duplicated spaces
    words = formatted_text.lower().split(" ")
    word_value_list = []

    for word in words:
        word_val_sum = 0
        for letter in word:
            word_val_sum += letter_num_dict[letter]

        word_value_list.append((word, word_val_sum))

    text_sum = 0
    for word_sum in word_value_list:
        text_sum += word_sum[1]

    print("Text sum = " + str(text_sum))
    print(word_value_list)


