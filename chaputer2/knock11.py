f = open("hightemp.txt", encoding="utf-8")
for i in f:
    print(i.replace("\t", " "), end="")
f.close()