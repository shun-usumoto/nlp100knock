with open("col1.txt", encoding="utf-8") as col1_file, \
        open("col2.txt", encoding="utf-8") as col2_file, \
        open("col3.txt", mode="w", encoding="utf-8") as col3_file:


    for col1_line, col2_line in zip(col1_file, col2_file):
        col3_file.write(col1_line.rstrip() + "\t" + col2_line)  # rstrip()で空白削除
