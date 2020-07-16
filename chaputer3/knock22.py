import re
from knock20 import britain

pattern = r"\[\[Category.*"
result = re.findall(pattern, britain())

for line in result:
    # [[Category:の文字列を空に置換
    name = re.sub(r"\[\[Category:", "", line)
    # |から始まる4文字を空に置換
    name = re.sub(r"\|...$", "", name)
    # ]]で終わる文字列を空に置換
    name = re.sub(r"]]$", "", name)
    print(name)
