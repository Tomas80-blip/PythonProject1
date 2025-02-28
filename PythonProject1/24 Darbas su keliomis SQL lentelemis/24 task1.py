# Parasyti
# ipython      enter

# atsiranda zalios spalvos  In [1]:

#pakeiciam konfiga kad graziau printintu
%config SqlMagic.style = '_DEPRECATED_DEFAULT'

# Sukuriame arba prisijungiame prie duombazes
%load_ext sql   # enter
%sql sqlite:///personal_cars.db   # enter


Uzduotis

# 1. Lentelių peržiūra ir analizė

# 1. Peržiūrėkite visų lentelių struktūrą ir išsiaiškinkite, kokius duomenis jos saugo.
# 2. Atrinkite 10 pirmųjų įrašų iš kiekvienos lentelės (person, car, company).
# 3. Atraskite visus unikalius automobilių gamintojus (make) iš car lentelės.

# 1. Peržiūrėkite visų lentelių struktūrą ir išsiaiškinkite, kokius duomenis jos saugo.
%%sql
SELECT name, sql FROM sqlite_master WHERE name NOT LIKE "sqlite%";

# 2. Atrinkite 10 pirmųjų įrašų iš kiekvienos lentelės (person, car, company).

%%sql
SELECT * FROM person LIMIT 10;

%%sql
SELECT * FROM car LIMIT 10;

%%sql
SELECT * FROM company LIMIT 10;

# 3. Atraskite visus unikalius automobilių gamintojus (make) iš car lentelės.

%%sql
SELECT DISTINCT make FROM car;

# 2. Lentelių jungimas naudojant WHERE

# 1. Suraskite visų žmonių vardus, pavardes ir jų vairuojamus automobilius (make,
# model).
# 2. Suraskite žmones, kurie neturi priskirto automobilio (car_id IS NULL).
# 3. Sujunkite visas tris lenteles (person, car, company) ir išveskite žmonių vardus,
# pavardes, jų automobilius ir kompanijos pavadinimą.

# 1. Suraskite visų žmonių vardus, pavardes ir jų vairuojamus automobilius (make,
# model).
%%sql
SELECT person.first_name, person.last_name, car.make,car.model
FROM person, car
WHERE person.car_id=car.id;

# 2. Suraskite žmones, kurie neturi priskirto automobilio (car_id IS NULL).

%%sql
SELECT first_name, last_name
FROM person
WHERE car_id IS NULL

# 3. Sujunkite visas tris lenteles (person, car, company) ir išveskite žmonių vardus,
# pavardes, jų automobilius ir kompanijos pavadinimą.

%%sql
SELECT person.first_name, person.last_name, car.make, car.model, company.name
FROM person, car, company
WHERE person.car_id=car.id AND person.company_id=company.id;

# atspausdina istorija
history

# baigus darba atsijungti
exit