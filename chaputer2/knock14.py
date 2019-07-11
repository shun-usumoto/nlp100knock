n = int(input("N:"))

with open("hightemp.txt", encoding="utf-8") as data_file:
    for index, line in enumerate(data_file):
        if index == n:
            break
        print(line.rstrip())