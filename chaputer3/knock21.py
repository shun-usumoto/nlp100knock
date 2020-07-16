import re
from knock20 import britain

# [[Categoryで始まる行をpatternに代入
pattern = r"\[\[Category.*"
# findall()でマッチする行をリスト化
result = re.findall(pattern, britain())

for line in result:
    print(line)