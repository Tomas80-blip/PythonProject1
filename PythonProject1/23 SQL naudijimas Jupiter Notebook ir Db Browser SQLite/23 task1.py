# SQL naudojimas Jupyter Notebook ir Db Browser SQLite be Python

# UZDUOTIS

# 1. SQL aplinkos paruošimas
# Užduotis:
# Įdiekite reikalingą ipython-sql modulį (pip install ipython-sql).
# Jupyter Notebook įkelkite SQL plėtinį ir prisijunkite prie mokykla.db duomenų bazės.
# %load_ext sql
# %sql sqlite:///mokykla.db
# Jei neturite duomenų bazės, sukurkite lentelę mokytojai su laukais:
# • id (pirminis raktas, INTEGER)
# • vardas (TEXT)
# • pavarde (TEXT)
# • dalykas (TEXT)
# • atlyginimas (INTEGER)

# 2. Duomenų atrinkimas (SELECT)
# Užduotis:
# Atrinkite visus mokytojus ir išveskite jų duomenis.
# Atrinkite mokytojus, kurie dėsto matematiką.
# %%sql
# SELECT * FROM mokytojai WHERE dalykas = 'Matematika';
# Atrinkite mokytojus, kurių atlyginimas didesnis nei 1500.
# Atrinkite tik mokytojų vardus ir pavardes.

# 3. Filtravimas su BETWEEN ir IN
# Užduotis:
# Atrinkite mokytojus, kurių atlyginimas yra tarp 1000 ir 2000.
# Atrinkite mokytojus, kurie dėsto "Lietuvių", "Anglų" arba "Istoriją".
# %%sql
# SELECT * FROM mokytojai WHERE atlyginimas BETWEEN 1000 AND 2000;
# Atrinkite mokytojus, kurie dėsto tik gamtos mokslus (pvz., "Biologiją" arba "Chemiją").

# 4. Paieška pagal teksto fragmentą (LIKE)
# Užduotis:
# Atrinkite mokytojus, kurių pavardė prasideda raide "J".
# Atrinkite mokytojus, kurių vardas baigiasi raide "s".
# %%sql
# SELECT * FROM mokytojai WHERE vardas LIKE '%s';
# Atrinkite mokytojus, kurių antra vardo raidė yra "e".


# 1. SQL aplinkos paruošimas

# Per terminala įdiekite reikalingą modulį (jei dar neįdiegtas)
!pip install ipython-sql

# Parasyti
ipython  # ENTER

# atsiranda zalios spalvos  In [1]:

# Įkeliame SQL plėtinį ir prisijungiame prie duomenų bazės
%load_ext sql  #  enter
%sql sqlite:///mokykla.db  #  enter

#pakeiciam konfiga kad graziau printintu
%config SqlMagic.style = '_DEPRECATED_DEFAULT'

# Jei duomenų bazė neegzistuoja, sukuriame lentelę mokytojai
%%sql
CREATE TABLE IF NOT EXISTS mokytojai (
    id INTEGER PRIMARY KEY,
    vardas TEXT,
    pavarde TEXT,
    dalykas TEXT,
    atlyginimas INTEGER
);


# po kiekvienos komandos spausti 2-3 kartus enter kad isirasytu
# ideti mokytoja
%%sql
INSERT INTO mokytojai (vardas, pavarde, dalykas, atlyginimas) VALUES
('Jonas', 'Jonaitis', 'Matematika', 1600);

%%sql
INSERT INTO mokytojai (vardas, pavarde, dalykas, atlyginimas) VALUES
('Petras', 'Petraitis', 'Fizika', 2000);

%%sql
INSERT INTO mokytojai (vardas, pavarde, dalykas, atlyginimas) VALUES
('Lukas', 'Lukaitis', 'Geografija', 1800);

%%sql
INSERT INTO mokytojai (vardas, pavarde, dalykas, atlyginimas) VALUES
('Simas', 'Simaitis', 'Lietuviu', 1900);

%%sql
INSERT INTO mokytojai (vardas, pavarde, dalykas, atlyginimas) VALUES
('Rokas', 'Rokaitis', 'Anglų', 1900);

%%sql
INSERT INTO mokytojai (vardas, pavarde, dalykas, atlyginimas) VALUES
('Asta', 'Astaite', 'Istorija', 2500);

%%sql
INSERT INTO mokytojai (vardas, pavarde, dalykas, atlyginimas) VALUES
('Laura', 'Lauraite', 'Biologija', 2400);

%%sql
INSERT INTO mokytojai (vardas, pavarde, dalykas, atlyginimas) VALUES
('Lina', 'Linaite', 'Chemija', 1400);

#arba kitaip ideti visa sarasas
# dest pridetas sarasas

%%sql
INSERT INTO mokytojai (vardas, pavarde, dalykas, atlyginimas) VALUES
(('Jonas', 'Jonaitis', 'Matematika', 1600),
 ('Petras', 'Petraitis', 'Lietuvių', 1400),
 ('Marius', 'Jankauskas', 'Istorija', 1200),
 ('Elena', 'Kavaliauskienė', 'Biologija', 1800),
 ('Simona', 'Simonaitytė', 'Chemija', 1100),
 ('Rita', 'Juodgalvė', 'Anglų', 2000),
 ('Tomas', 'Jurgelevičius', 'Matematika', 1700),
 ('Aistis', 'Bieliauskas', 'Fizika', 900),
 ('Eglė', 'Žilinskaitė', 'Anglų', 1300),
 ('Vytas', 'Grigonis', 'Lietuvių', 1550),
 ('Darius', 'Medelis', 'Chemija', 1450),
 ('Justina', 'Jakutytė', 'Istorija', 1750),
 ('Gabrielė', 'Kučinskaitė', 'Matematika', 1250),
 ('Saulius', 'Januškevičius', 'Fizika', 1900),
 ('Edvinas', 'Kvedaras', 'Lietuvių', 1000));


# 2. Duomenų atrinkimas (SELECT)

# Atvaizduojame visus mokytojus
%%sql
SELECT * FROM mokytojai;

# Atrenkame mokytojus, kurie dėsto matematiką
%%sql
SELECT * FROM mokytojai WHERE dalykas = 'Matematika';

# Atrenkame mokytojus, kurių atlyginimas didesnis nei 1500
%%sql
SELECT * FROM mokytojai WHERE atlyginimas > 1500;

# Atrenkame tik mokytojų vardus ir pavardes
%%sql
SELECT vardas, pavarde FROM mokytojai;

# 3. Filtravimas su BETWEEN ir IN

# Atrenkame mokytojus, kurių atlyginimas yra tarp 1000 ir 2000
%%sql
SELECT * FROM mokytojai WHERE atlyginimas BETWEEN 1000 AND 2000;

# Atrenkame mokytojus, kurie dėsto "Lietuvių", "Anglų" arba "Istoriją"
%%sql
SELECT * FROM mokytojai WHERE dalykas IN ('Lietuvių', 'Anglų', 'Istorija');

# Atrenkame mokytojus, kurie dėsto tik gamtos mokslus (pvz., "Biologiją" arba "Chemiją")
%%sql
SELECT * FROM mokytojai WHERE dalykas IN ('Biologija', 'Chemija');

# 4. Paieška pagal teksto fragmentą (LIKE)

# Atrenkame mokytojus, kurių pavardė prasideda raide "J"
%%sql
SELECT * FROM mokytojai WHERE pavarde LIKE 'J%';

# Atrenkame mokytojus, kurių vardas baigiasi raide "s"
%%sql
SELECT * FROM mokytojai WHERE vardas LIKE '%s';

# Atrenkame mokytojus, kurių antra vardo raidė yra "e"
%%sql
SELECT * FROM mokytojai WHERE vardas LIKE '_e%';

# atspausdina istorija
history

# baigus darba atsijungti
exit