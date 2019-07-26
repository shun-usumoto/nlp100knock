import sys
f = open(sys.argv[1], encoding="utf-8")
for i in f:
    print(i.replace("\t", " ").rstrip())
f.close()