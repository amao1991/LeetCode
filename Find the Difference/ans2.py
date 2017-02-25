import sys

string_1 = sys.argv[1]
string_2 = sys.argv[2]

list_1 = list(string_1)
list_2 = list(string_2)

long_string = []

if len(list_1) >= len(list_2):
    long_string = list_1
else:
    long_string = list_2

different_char = ' '

for i in long_string:
    if string_1.count(i) != string_2.count(i):
        different_char = i
        print different_char

