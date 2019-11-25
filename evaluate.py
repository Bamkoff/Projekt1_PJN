#/bin/
import re
#oaa
right_marks = []
generated_mark = []


def grade_text(text):
    return 6

def evaluate(r_m, g_k):
    error_sum = 0.0
    for i in range(len(r_m)):
        if r_m[i] > g_k[i]: error_sum += float(r_m[i]) - float(g_k[i])
        else: error_sum += float(g_k[i]) - float(r_m[i])
    return error_sum/float(len(r_m))

with open("data/reviews") as file:
    for line in file:
        text = re.search(r'^([0-9]+)( *|-*)([^0-9].*)', line.replace('\n', ''))
        right_marks.append(int(text.group(1)))
        generated_mark.append(grade_text(text.group(3)))
file.close()

print(evaluate(right_marks, generated_mark))