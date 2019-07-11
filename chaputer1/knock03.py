s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

s = s.replace('.', "")
s = s.replace(',', "")
l = s.split()

x = []

for word in l:
    x.append(len(word))

print(x)

