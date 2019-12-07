import nltk
from re import search
import os
from math import log
# nltk.download('punkt')

dictionary = {}
number_of_lines = 0

with open("data/reviews", "r") as reviews:
    for line in reviews:
        match = search(r'^[0-9]+[ \-]+(.+)', line)
        if match is not None:
            tokens = nltk.word_tokenize(match.group(1))
            word_set = set();
            for word in tokens:
                word_set.add(word)
            for word in word_set:
                if word in dictionary:
                    dictionary[word] += 1
                else:
                    dictionary[word] = 1
            number_of_lines += 1
reviews.close()

for word in dictionary:
    dictionary[word] = log(float(number_of_lines)/float(dictionary[word]))

print(len(dictionary))
# print(dictionary['się'])
print(number_of_lines, int(os.popen("wc -l < data/reviews").read()) - 1)

with open("data/dictionary", "a") as dict:
    for word in dictionary:
        dict.write(word + " " + str(dictionary[word]) + "\n")