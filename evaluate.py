#/bin/
import re, os
#oaa
right_marks = []
generated_mark = []


def grade_text(text):
    f = open("data_transfer", "w")
    f.write(text)
    f.close()
    output = float(os.popen("vw -i data/wabbit_review_model data_transfer -p /dev/stdout --quiet").read())
    return output

def evaluate(r_m, g_m):
    error_sum = 0.0
    for i in range(len(r_m)):
        if r_m[i] > g_m[i]: error_sum += float(r_m[i]) - float(g_m[i])
        else: error_sum += float(g_m[i]) - float(r_m[i])
    return error_sum/float(len(r_m))

with open("data/wabbit_sets/wabbit_testing_set") as file:
    for line in file:
        text = re.search(r'^([0-9]+)( *|-*)([^0-9].*)', line.replace('\n', ''))
        right_marks.append(int(text.group(1)))
        generated_mark.append(grade_text(text.group(3)))
file.close()

print(evaluate(right_marks, generated_mark))