s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. " \
    "New Nations Might Also Sign Peace Security Clause. Arthur King Can. "

l = s.split()
result = {}

for i, k in enumerate(l, 1):
    if i in {1, 5, 6, 7, 8, 9, 15, 16, 19}:
        result[k[:1]] = i
    else:
        result[k[:2]] = i

print(result)