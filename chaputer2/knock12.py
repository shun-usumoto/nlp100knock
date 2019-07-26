import sys
with open(sys.argv[1], encoding="utf-8") as data_file, \
        open("col2.txt", mode="w", encoding="utf-8") as col1_file, \
        open("col3.txt", mode="w", encoding="utf-8") as col2_file:
    # for文で１行ずつ書き出す
    for line in data_file:
        # splitでリスト化してからスライスでインデックスを指定
        cols = line.split("\t")
        col1_file.write(cols[0] + "\n")
        col2_file.write(cols[1] + "\n")
