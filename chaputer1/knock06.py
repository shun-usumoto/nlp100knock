from knock05 import n_gram

s1 = "paraparaparadise"
s2 = "paragraph"

set_x = set(n_gram(s1, 2))
set_y = set(n_gram(s2, 2))

union = set_x.union(set_y)  # 和集合
intersection = set_x.intersection(set_y)  # 積集合
difference = set_x.difference(set_y)  # 差集合


print("X ∪ Y:" + str(union))
print("X ∩ Y:" + str(intersection))
print("X - Y" + str(difference))
print("Xの中にseは含まれるか:" + str("se" in set_x))
print("Yの中にseは含まれるか:" + str("se" in set_y))
