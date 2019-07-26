import sys
with open(sys.argv[1], encoding="utf-8") as data_file:
    s = set()

    for lines in data_file:
        line = lines.split("\t")
        s.add(line[0])

for i in s:
    print(i)