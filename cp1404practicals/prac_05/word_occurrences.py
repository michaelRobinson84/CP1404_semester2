print("Type a sentence to count word occurrence")
str_to_count = input("Text: ")
lst_words_to_count = str_to_count.split(" ")
lst_words_to_count = sorted(lst_words_to_count)

word_to_count = {}

for word in lst_words_to_count:
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1

longest_word = 0

for word in word_to_count.keys():
    current_word_length = len(word)
    if current_word_length > longest_word:
        longest_word = current_word_length

print("Longest word is " + str(longest_word))

for word in word_to_count.keys():
    word_with_colon = word + " : "
    print("{:{}} {}".format(word_with_colon, longest_word + 3, word_to_count[word]))
