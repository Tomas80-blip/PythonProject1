# uzduotis 3 Sąrašų iteravimas
# Sukurkite sąrašą su mėnesiais: ["sausis", "vasaris", "kovas",
# "balandis"].
# Naudokite for ciklą, kad atspausdintumėte kiekvieną mėnesį su prierašu "
# mėnuo".
# Sukurkite sąrašą su skaičiais: [5, 10, 15, 20].
# Suskaičiuokite visų skaičių sumą ir atspausdinkite ją.
# Padauginkite kiekvieną skaičių iš 2 ir išveskite rezultatą.


menesiai = ['sausis','vasaris','kovas','balandis']

for elem in menesiai:
    # print ('menuo' + elem)
    print (f'menuo {elem}')

skaiciai = [5,10,15,20]
suma = 0
for elem in skaiciai:
    suma += elem
    print(suma)
    print(elem * 2)

customer = 1
date = '2024-01-15'
order_number = 123
# a = 'Hello, dear' + customer + 'today is' + date + 'and we are still waiting your payment for order number' + order_number
# print(a)
a = f'Hello, dear {customer} today is {date} and we are still waiting your payment for order number {order_number}'
print (a)