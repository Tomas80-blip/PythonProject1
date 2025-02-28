





# Parasyti
# ipython      enter

# atsiranda zalios spalvos  In [1]:

#pakeiciam konfiga kad graziau printintu
%config SqlMagic.style = '_DEPRECATED_DEFAULT'

# Sukuriame arba prisijungiame prie duombazes
%load_ext sql   # enter
%sql sqlite:///personal_cars.db   # enter


# 5. JOIN variantai (LEFT JOIN, INNER JOIN)
# 1. Raskite visus žmones, įskaitant tuos, kurie neturi automobilio (LEFT JOIN).
# 2. Raskite visus žmones, įskaitant tuos, kurie neturi kompanijos (LEFT JOIN).
# 3. Raskite tik tuos žmones, kurie turi tiek automobilį, tiek priskirtą kompaniją (INNER
# JOIN).

# 1. Raskite visus žmones, įskaitant tuos, kurie neturi automobilio (LEFT JOIN).

%%sql
SELECT person.first_name, person.last_name, car.make, car.model
FROM person
LEFT JOIN car ON person.car_id = car.id


# 2. Raskite visus žmones, įskaitant tuos, kurie neturi kompanijos (LEFT JOIN).

%%sql
SELECT person.first_name, person.last_name, company.name
FROM person
LEFT JOIN company ON person.company_id=company.id

# 3. Raskite tik tuos žmones, kurie turi tiek automobilį, tiek priskirtą kompaniją (INNER
# JOIN)

%%sql
SELECT person.first_name, person.last_name, car.make, car.model, company.name
FROM person
JOIN car ON person.car_id = car.id
JOIN company ON person.company_id=company.id

# atspausdina istorija
history

# baigus darba atsijungti
exit