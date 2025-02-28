# 5. Specifinių funkcijų importavimas su alias
# Užduotis 5:
# Sukurkite Python programą, kuri:
# 1. Importuoja sqrt funkciją iš math modulio su alias sq.
# 2. Apskaičiuoja kvadratinę šaknį iš 625 naudojant sq().
# 3. Išspausdina rezultatą.

from math import sqrt as sq

result = sq(625)

# Išspausdiname rezultatą
print("Kvadratinė šaknis iš 625 yra:", result)

# 6. Visko importavimas iš modulio (nerekomenduojamas būdas)
# Užduotis 6:
# 1. Sukurkite Python programą, kuri naudoja from math import *.
# 2. Apskaičiuoja sinusą iš 90 laipsnių (naudojant sin()).
# 3. Išspausdina rezultatą.
# 4. Parašykite komentaruose, kodėl šis metodas gali būti pavojingas dideliuose
# projektuose.

# Importuojame visas math modulio funkcijas
from math import *

# Apskaičiuojame sinusą iš 90 laipsnių (90 laipsnių = pi/2 radianų)
result = sin(radians(90))

# Išspausdiname rezultatą
print(f"Sinusas iš 90 laipsnių yra: {result}")

# Komentaras apie importavimo metodo pavojų:
# Naudojant "from math import *" galima perrašyti kitų programos modulių funkcijas
# arba kintamuosius, nes visi math modulio vardai tiesiogiai įtraukiami į dabartinę
# vardų sritį. Dideliuose projektuose tai gali sukelti konfliktus ir klaidas,
# kurios sunkiai aptinkamos. Vietoj šio metodo rekomenduojama naudoti "import math"
# arba "from math import specific_function", kad būtų išvengta vardų konfliktų.