import re, os, sys, nltk

def create_wabbit_data_set(file_path):
    with open("data/" + file_path, "r") as learning_set:
        wabbit_learn_data = open("data/wabbit_" + file_path, "a")
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
            if re_line.group(1) == "1" or re_line.group(1) == "10" or re_line.group(1) == "2":
                wabbit_line = re_line.group(1) + " 2 |"
            else:
                wabbit_line = re_line.group(1) + " |"
            for token in tokens:
                wabbit_line += " " + token + ":." + str(dict[token])
            # print(wabbit_line)
            wabbit_learn_data.write(wabbit_line + '\n')

create_wabbit_data_set("learning_set")
create_wabbit_data_set("testing_set")
create_wabbit_data_set("production_set")

os.popen("vw data/wabbit_learning_set -f data/wabbit_review_model")