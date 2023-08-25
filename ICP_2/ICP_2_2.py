import re

freq_word = {}
text_read = open('input.txt', 'r')
text_string = text_read.read().lower()
match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)
for word in match_pattern:
    count = freq_word.get(word, 0)
    freq_word[word] = count + 1

frequency_list = freq_word.keys()

f = open("output.txt", "w")
for words in frequency_list:
    result = words + " " + str(freq_word[words])
    f.write(result + "\n")