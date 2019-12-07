import re
import os
import sys
import nltk

dictionary = {}

with open("data/dictionary", "r") as dict:
    for line in dict:
        match = re.search(r'^([^ ]+) (.+)', line)
        if match is not None:
            dictionary[match.group(1)] = float(match.group(2))
dict.close()


def create_wabbit_data_set(file_path):
    with open("data/sets/" + file_path, "r") as learning_set:
        wabbit_learn_data = open("data/wabbit_sets/wabbit_" + file_path, "a")
        for line in learning_set:
            re_line = re.search(r'^([0-9]+)( *|-*)([^0-9].*)', line.replace('\n', ' ').lower().replace(':', ' '))
            tokens = nltk.word_tokenize(re_line.group(3))
            for token in range(len(tokens)-1, -1, -1):
                if len(tokens[token]) <= 3:
                    tokens.pop(token)
                # elif re.search(r'^.*[./\\\'\"\>\<`~]*.*$|^..$|^.$', tokens[token]) is not None:
                #     tokens.pop(token)
            # print(tokens)
            dict = {}
            for token in tokens:
                if token in dict:
                    dict[token] += 1
                else:
                    dict[token] = 1
                wabbit_line = re_line.group(1) + " |f"
            for token in tokens:
                if token in dictionary:
                    wabbit_line += " " + token + ":" + str(float(dict[token]) * dictionary[token])
                else:
                    wabbit_line += " " + token + ":" + str(dict[token] * 1)
            # print(wabbit_line)
            wabbit_learn_data.write(wabbit_line + '\n')


create_wabbit_data_set("learning_set")
create_wabbit_data_set("testing_set")
create_wabbit_data_set("production_set")

# os.popen("vw data/wabbit_sets/wabbit_learning_set -f data/wabbit_review_model")
