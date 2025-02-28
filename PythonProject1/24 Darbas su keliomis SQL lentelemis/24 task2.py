# Parasyti
# ipython      enter

# atsiranda zalios spalvos  In [1]:

#pakeiciam konfiga kad graziau printintu
%config SqlMagic.style = '_DEPRECATED_DEFAULT'

# Sukuriame arba prisijungiame prie duombazes
%load_ext sql   # enter
%sql sqlite:///personal_cars.db   # enter


# 3. Lentelių jungimas naudojant JOIN
# 1. Išveskite žmonių vardus, pavardes ir jų automobilius naudojant JOIN.
# 2. Rikiuokite rezultatą pagal automobilio markę (make).
# 3. Pridėkite ir kompanijos pavadinimą į užklausą.

# 1. Išveskite žmonių vardus, pavardes ir jų automobilius naudojant JOIN.

%%sql
SELECT first_name, last_name, email, make, model
FROM person
JOIN car ON person.car_id=car.id;

# 2. Rikiuokite rezultatą pagal automobilio markę (make).

%%sql
SELECT first_name, last_name, email, make, model
FROM person
JOIN car ON person.car_id=car.id
ORDER BY make;

# 3. Pridėkite ir kompanijos pavadinimą į užklausą.

%%sql
SELECT first_name, last_name, email, make, model, company.name
FROM person
JOIN car ON person.car_id=car.id
JOIN company ON person.company_id=company.id
ORDER BY company.name;

# 4. Grupavimas ir skaičiavimai
# 1. Suskaičiuokite, kiek žmonių dirba kiekvienoje kompanijoje.
# 2. Suskaičiuokite, kiek žmonių neturi priskirto automobilio.


# 1. Suskaičiuokite, kiek žmonių dirba kiekvienoje kompanijoje.

%%sql
SELECT name, COUNT() AS "people"
FROM person
JOIN company ON person.company_id=company.id
GROUP BY name
ORDER BY people DESC;

# 2. Suskaičiuokite, kiek žmonių neturi priskirto automobilio.

%%sql
SELECT COUNT(*) AS "people_no_auto"
FROM person
WHERE car_id IS NULL;

# atspausdina istorija
history

# baigus darba atsijungti
exit