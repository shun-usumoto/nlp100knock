import sys
f = open(sys.argv[1], encoding="utf-8")
print(len(f.readlines()))
f.close()