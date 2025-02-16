# 5. Datos ir laiko įvedimas naudojant str formatą
# Užduotis 5:
# Paprašykite vartotojo įvesti datą formatu "YYYY-MM-DD".
# Konvertuokite įvestą tekstą į datetime objektą naudojant strptime().
# Išveskite datą datetime formatu.


from datetime import datetime

ivesta_data = input("Įveskite datą formatu 'YYYY-MM-DD': ")


try:
    data_obj = datetime.strptime(ivesta_data, "%Y-%m-%d")
    print("Įvesta data datetime formatu:", data_obj)
except ValueError:
    print("Neteisingas datos formatas. Prašome įvesti datą teisingu formatu.")


import datetime

# ivestis = input('Iveskite data formatu YYYY-MM-DD: ')
# my_date_object = datetime.datetime.strptime(ivestis, "%Y-%m-%d")
# print(f'Data datetime formatu: {my_date_object}')


# 6. Datos ir laiko išvedimas naudojant strftime formatą
# Užduotis 6:
# Sukurkite datetime objektą: 2022-12-31, 23:59:59.
# Naudodami strftime(), suformatuokite ir išveskite:
# "31/12/2022 23:59:59"
# "2022 metų gruodžio 31 diena"

from datetime import datetime

data_laikas = datetime(2022, 12, 31, 23, 59, 59)

formatted_1 = data_laikas.strftime("%d/%m/%Y %H:%M:%S")
print(formatted_1)

menesiai = {
    1: "sausio", 2: "vasario", 3: "kovo", 4: "balandžio",
    5: "gegužės", 6: "birželio", 7: "liepos", 8: "rugpjūčio",
    9: "rugsėjo", 10: "spalio", 11: "lapkričio", 12: "gruodžio"
}

formatted_2 = f"{data_laikas.year} metų {menesiai[data_laikas.month]} {data_laikas.day} diena"
print(formatted_2)