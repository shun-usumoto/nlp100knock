import re
from knock20 import britain

# 先頭から"="が1回以上繰り返し、文末が"="の文字列をパターン化
pattern = r"^=+.*=$"
# 複数行モードを使用
result = re.findall(pattern, britain(), re.MULTILINE)

for i in result:
    # 各行の"="の数の合計 / 2 - 1
    count = int(i.count("=") / 2 - 1)
    print(i.replace("=", "").strip() + ":" + str(count))
