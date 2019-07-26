import sys
n = int(sys.argv[2])

if n > 0:
    with open(sys.argv[1], encoding="utf-8") as data_file:
        lines = data_file.readlines()

    for i in lines[-n:]:
        print(i.rstrip())