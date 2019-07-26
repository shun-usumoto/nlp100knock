import sys
n = int(sys.argv[2])

with open(sys.argv[1], encoding="utf-8") as data_file:
    for index, line in enumerate(data_file):
        if index == n:
            break
        print(line.rstrip())