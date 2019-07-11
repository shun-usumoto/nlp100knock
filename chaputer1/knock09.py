import random

s = "I couldn't believe that I could actually understand what I was reading : " \
    "the phenomenal power of the human mind ."

l = s.split()
result = []

for word in l:
    if len(word) <= 4:
        result.append(word)
    else:
        random_list = list(word[1:-1])
        random.shuffle(random_list)
        result.append(word[0] + "".join(random_list) + word[-1])

print(" ".join(result))


