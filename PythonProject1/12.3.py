# Sukurkite programą, kuri:
# # 1. Prašo vartotojo įvesti skaičių.
# # 2. Bandys konvertuoti į int.
# # 3. Jei klaidos nėra, naudos else, kad atspausdintų "Konversija sėkminga:
# # <skaičius>".
# # 4. finally bloke atspausdins "Programa baigė darbą.", nepriklausomai nuo
# # klaidų.


while True:
        try:
                ivestis = input("Įveskite integer skaičių: ")
                int_skaicius = int(ivestis)
                print("Įvestis tinkama", int_skaicius)
        except ValueError:
                print("Įvestis NETINKAMA, pakartokite!!!")
        else:
                print(f'Konversija sėkminga: {int_skaicius}')
        finally:
                print("Programa baigė darbą")