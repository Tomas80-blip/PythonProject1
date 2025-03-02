# Elif ir kelių sąlygų tikrinimas
# 1. Parašykite programą, kuri patikrina vartotojo įvestą balą:
# a. Jei balas tarp 0–4, spausdina „Nepatenkinamas“.
# b. Jei balas tarp 5–7, spausdina „Vidutinis“.
# c. Jei balas tarp 8–10, spausdina „Puikus“.

balas = int(input('Iveskite bala:'))
if 0 <= balas <= 4:
    print(f'Nepatenkinamas')
elif 5 <= balas <= 7:
    print(f'Vidutinis')
elif 8 <= balas <= 10:
    print(f'Puikus')

# 2. Sukurkite programą, kuri leidžia vartotojui įvesti metų laiką (pvz., „Žiema“,
# „Pavasaris“). Priklausomai nuo įvesto laiko, spausdinkite atitinkamus mėnesius.

ketvirtis = input('Iveskite metu laika:')
if ketvirtis == "Ziema":
    print('Gruodis', 'Sausis', 'Vasaris')
elif ketvirtis == "Pavasaris":
    print('Kovas', 'Balandis', 'Geguzis')
elif ketvirtis == "Vasara":
    print('Birzelis', 'Liepa', 'Rugpjutis')
elif ketvirtis == "Ruduo":
    print('Rugsejis', 'Spalis', 'Lapkritis')


# sudetingesnis variantas
balas = int(input('Įveskite balą: '))

res = 'Neteisingas įvestas skaičius'
if 0 <= balas <= 4:
    res = 'Nepatenkinamas'
elif 5 <= balas <= 7:
    res = 'Vidutinis'
elif 8 <= balas <= 10:
    res = 'Puikus'

print(res)

sezonas = input('Įveskite metų laiką: ').strip().lower()

menesiai = 0
if sezonas == 'žiema':
    menesiai = ['gruodis', 'sausis', 'vasaris']
elif sezonas == 'pavasaris':
    menesiai = ['kovas', 'balandis', 'gegužė']
elif sezonas == 'vasara':
    menesiai = ['birželis', 'liepa', 'rugpjūtis']
elif sezonas == 'ruduo':
    menesiai = ['rugsėjis', 'spalis', 'lapkritis']

if menesiai:
    print(', '.join(menesiai))
else:
    print('Turėjote įvesti galiojantį metų laiką.')