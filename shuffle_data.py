# distributes reviews for AI learning and testing

import re
import os

# get number of lines from file data/reviews
number_of_lines = int(os.popen("wc -l < data/reviews").read())
# print(number_of_lines)

# 80% from reviews goes to learning set for vw(vowpal wabbit)
learning_set = int(0.8 * number_of_lines)
# print(learning_set)

# from 80% to 90% goes to testing set to test how the learning proceeds
testing_set = int(0.9 * number_of_lines)
# print(testing_set)

# rest goes to production set to check overfitting

with open("data/reviews", "r") as reviews:
    # number of line in file
    line_nr = 1

    # file with learning set
    l_s = open("data/sets/learning_set", "a")

    # file with test set
    t_s = open("data/sets/testing_set", "a")

    # file with production set
    p_s = open("data/sets/production_set", "a")

    for line in reviews:
        text = re.search(r'^([0-9]+)( *|-*)([^0-9].*)', line.replace('\n', ''))
        if text is not None:
            if line_nr <= learning_set:
                l_s.write(text.group(1) + " " + text.group(3) + "\n")
            elif line_nr <= testing_set:
                t_s.write(text.group(1) + " " + text.group(3) + "\n")
            else:
                p_s.write(text.group(1) + " " + text.group(3) + "\n")
            line_nr += 1

    l_s.close()
    t_s.close()
    p_s.close()
    reviews.close()