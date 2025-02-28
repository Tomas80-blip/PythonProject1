# 4. Generatoriai
# Užduotis:
# Sukurkite generatorių fib_generator(n), kuris grąžina pirmus n Fibonacci skaičius.
# • Fibonacci seka: 0, 1, 1, 2, 3, 5, 8, 13, …
# Papildoma užduotis:
# Sukurkite generatorių filtruoti_lyginius(seka), kuris iš pateiktos skaičių sekos
# grąžina tik lyginius skaičius.


# Fibonacci generatorius
def fib_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Generatorius, filtruojantis lyginius skaičius
def filtruoti_lyginius(seka):
    for skaicius in seka:
        if skaicius != 0 and skaicius % 2 == 0:
            yield skaicius

# Pavyzdys, kaip naudoti abu generatorius
n = 10
fibonacci_seka = fib_generator(n)
lyginiu_skaiciu_seka = filtruoti_lyginius(fibonacci_seka)

# Atspausdiname rezultatus
print("Pirmi", n, "Fibonacci skaičiai:")
print(list(fib_generator(n)))

print("\nTik lyginiai Fibonacci skaičiai:")
print(list(filtruoti_lyginius(fib_generator(n))))