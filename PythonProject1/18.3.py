# 3. Iteratoriai
# Užduotis:
# Sukurkite klasę SkaiciuSekosIteratorius, kuri:
# 1. Inicializuojama su pradiniu ir galiniu skaičiumi.
# 2. Leidžia iteruoti nuo pradinio iki galinio skaičiaus imtinai.
# 3. Grąžina skaičius kas antrą žingsnį.
# Papildoma užduotis:
# Pridėkite metodą atgaline_seka(), kuris grąžina skaičius atvirkštine tvarka.

class SkaiciuSekosIteratorius:
    def __init__(self, pradinis, galinis):
        self.pradinis = pradinis
        self.galinis = galinis

    def __iter__(self):
        return iter(range(self.pradinis, self.galinis + 1, 2))

    def atgaline_seka(self):
        return [i for i in range(self.galinis, self.pradinis - 1, -2)]

# Pavyzdys naudojimui
skaiciai = SkaiciuSekosIteratorius(1, 10)

print("Sekos iteravimas:")
for skaicius in skaiciai:
    print(skaicius)

print("Atgalinė seka:")
print(skaiciai.atgaline_seka())