# Simbolių indeksavimas
text1 = 'ABCDE'
print(text1[0])
print(text1[1])
print(text1[2])
print(text1[3])
print(text1[4])
print('-----------')
print(text1[-1])
print(text1[-2])

# Slicing
text1 = 'ABCDE'
print(text1[0:2])
print(text1[1:4])
print(text1[1:-1])
print(text1[1:])
print(text1[:4])

# Task slice "Hello World"
# Hello
# Hello
# World
# Hello W
# ello W
# ello Worl
# ' ' - Tarpas

text2 = 'Hello World'
print(text2[:5])
print(text2[0:5])
print(text2[6:])
print(text2[:7])
print(text2[1:7])
print(text2[1:-1])
print("'" + text2[5] + "'")
print('Task done!')
