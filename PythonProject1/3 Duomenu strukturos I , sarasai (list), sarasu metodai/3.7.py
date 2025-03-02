# String metodai sąrašams
# 1. Naudokite eilutę "obuolys bananai kriaušės".
# a. Paverskite ją sąrašu, naudodami .split() metodą.
# b. Naudodami .join(), sujunkite sąrašo elementus į vieną eilutę su
# skiriamąja linija ---.

vaisiai_str = 'obuolys bananai kriause'
print(vaisiai_str)

vaisiai_list = vaisiai_str.split(" ")
print(vaisiai_list)

joined_str = "---".join(vaisiai_list)
print(joined_str)
print(type(joined_str))