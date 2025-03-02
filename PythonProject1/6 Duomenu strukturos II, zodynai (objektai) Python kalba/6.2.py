# Duomenu pasalinimas ir reiksmiu keitimas
#
# Turite si zodyna apie elektronime parduotuve:

# 1. Pasalinkite kategorija "Clothing" is saraso kategoriju.
# 2. Sumazinkite kiekvieno produkto kaina 5%, jei jo kaina yra didesne nei 50.
# 3. Padidinkite produkto "Laptop" sandelio kieki iki 15.
# 4. Jei parduotuves ivertinimas(rating) yra mazesnis nei 4.6, padidinkite ji 0.1

store = {
    "name": "E-Shop",
    "categories": ["Electronics", "Books", "Clothing"],
    "products": [
        {"name": "Laptop", "price": 1000, "stock": 10},
        {"name": "Book", "price": 20, "stock": 50},
        {"name": "T-shirt", "price": 15, "stock": 100}
    ],
    "rating": 4.5
}

print(store)

store ["categories"].remove ("Clothing")
print(store)

for product in store["products"]:
    if product ['price'] > 50:
        product ['price'] *= 0.95
print(store)

for product in store ['products']:
    if product['name'] == 'Laptop':
        product['stock'] = 15
print(store)

if store["rating"] < 4.6:
    store["rating"] += 0.1
print(store)
