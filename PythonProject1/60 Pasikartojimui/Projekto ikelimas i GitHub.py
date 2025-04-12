# Django! Upload final project to GIT
# Ką reikia padaryti prieš keliant projektą į GitHub
# Prieš įkeliant savo projektą į GitHub, įsitikinkite, kad atlikote šiuos žingsnius:
#
# 1. Prijunkite projektą prie GitHub repozitorijos
# Sukurkite naują repozitoriją GitHub platformoje.
# Savo projekte terminale įvykdykite:
# git init
# git remote add origin https://github.com/vartotojo-vardas/jusu-repozitorija.git
# git add .
# git commit -m "Initial commit"
# git push -u origin master

# 2. Sukurkite .gitignore failą
# Į jį įtraukite visus failus ir katalogus, kurių nereikia kelti į GitHub. Pavyzdys:
# __pycache__/
# *.pyc
# .env
# node_modules/
# venv/

# 3. Sukurkite requirements.txt
# Jame turi būti visos bibliotekos, kurias naudojote projekte. Sukurti galima su komanda:
# pip freeze > requirements.txt

# 4. Paruoškite README.md failą
# Šiame faile turi būti:
# Projekto pavadinimas ir trumpas aprašymas
# Technologijos, kurios buvo naudotos (pvz. Python, Flask, Django, React ir pan.)
# Instrukcija, kaip paleisti projektą savo kompiuteryje

# Pavyzdys:
# ## Projekto paleidimas
#
# 1. Atsisiųskite repozitoriją:
# git clone https://github.com/vartotojo-vardas/jusu-repozitorija.git cd jusu-repozitorija
#
#
# 2. Sukurkite virtualią aplinką:
# python -m venv venv source venv/bin/activate # Windows naudokite: venv\Scripts\activate
#
#
# 3. Įidiekite reikalingas bibliotekas:
# pip install -r requirements.txt
#
#
# 4. Paleiskite projektą (priklausomai nuo projekto tipo):
# - Flask: `python app.py`
# - Django: `python manage.py runserver`