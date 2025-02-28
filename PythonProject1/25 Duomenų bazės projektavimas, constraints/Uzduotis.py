# 1. Lentelės kūrimas
# Užduotis:
# Sukurkite naują lentelę teacher, kuri turės šiuos stulpelius:
# • id (INTEGER, pirminis raktas, unikalus),
# • f_name (TEXT, negali būti NULL),
# • l_name (TEXT, negali būti NULL),
# • email (TEXT, unikalus),
# • subject (TEXT, negali būti NULL),
# • years_experience (INTEGER, gali būti NULL).
# Įterpkite bent 3 mokytojų įrašus ir patikrinkite, ar lentelė sukurta teisingai.

ipython

%load_ext sql

%sql sqlite:///school.db

%config SqlMagic.style = '_DEPRECATED_DEFAULT'



%%sql
CREATE TABLE teacher(
    id INTEGER PRIMARY KEY UNIQUE,
    f_name TEXT NOT NULL,
    l_name TEXT NOT NULL,
    email TEXT UNIQUE,
    subject TEXT NOT NULL,
    years_experience  INTEGER
);

# Tikrinam value reiksmes
%%sql
SELECT name, sql FROM sqlite_master WHERE name NOT LIKE "sqlite%";

%%sql
INSERT INTO teacher (id, f_name, l_name, email, subject, years_experience) VALUES
(1, 'Jonas', 'Petraitis', 'jonas.petraitis@example.com', 'Matematika', 10),
(2, 'Ona', 'Kazlauskienė', 'ona.kazlauskiene@example.com', 'Lietuvių kalba', 15),
(3, 'Marius', 'Jonaitis', 'marius.jonaitis@example.com', 'Fizika', 8);

%%sql
SELECT * FROM teacher;

# Panaikinkime lentelę coder ir sukurkime ją iš naujo su apribojimais:
%%sql
DROP TABLE IF EXISTS teacher;

# Tikrinam
%%sql
SELECT * FROM teacher;


# 2. CONSTRAINTS taikymas
# Užduotis:
# Sukurkite naują lentelę student, kuri turės apribojimus:
# • id (INTEGER, pirminis raktas),
# • f_name (TEXT, negali būti NULL),
# • l_name (TEXT, negali būti NULL),
# • email (TEXT, turi būti unikalus),
# • age (INTEGER, turi būti daugiau nei 6),
# • class (TEXT, numatytoji reikšmė "1A"),
# Įterpkite įrašą su age = 5 ir paaiškinkite, kokią klaidą gavote.
# Įterpkite įrašą be class reikšmės ir patikrinkite, kokia reikšmė bus naudojama.


%%sql
CREATE TABLE student (
    id INTEGER PRIMARY KEY,
    f_name TEXT NOT NULL,
    l_name TEXT NOT NULL,
    email TEXT UNIQUE,
    age INTEGER CHECK (age > 6),
    class TEXT DEFAULT '1A'
);

# Įterpkite įrašą su age = 5 ir paaiškinkite, kokią klaidą gavote.
%%sql
INSERT INTO student (id, f_name, l_name, email, age)
VALUES (1, 'Jonas', 'Petrauskas', 'jonas@email.com', 5);
# CHECK constraint failed: age > 6
# įrašas su age = 5 negali būti įterptas, nes neatitinka šios sąlygos.

%%sql
INSERT INTO student (id, f_name, l_name, email, age)
VALUES (2, 'Petras', 'Jonaitis', 'petras@email.com', 10)

# Tikrinam
%%sql
SELECT * FROM student;


# 3. ALTER TABLE naudojimas
# Užduotis:
# 1. Pridėkite naują stulpelį gender į student lentelę (TEXT, gali būti NULL).
# 2. Pervadinkite stulpelį class į grade.
# 3. Ištrinkite stulpelį email iš teacher lentelės.
# 4. Naudokite PRAGMA table_info(student); ir patikrinkite atliktus pakeitimus.

# 1. Pridėkite naują stulpelį gender į student lentelę (TEXT, gali būti NULL).
%%sql
ALTER TABLE student ADD COLUMN gender TEXT;

%%sql
SELECT * FROM student;

# 2. Pervadinkite stulpelį class į grade.

%%sql
ALTER TABLE student RENAME COLUMN class TO grade;

# Tikrinam value reiksmes
%%sql
SELECT name, sql FROM sqlite_master WHERE name NOT LIKE "sqlite%";

# 3. Ištrinkite stulpelį email iš teacher lentelės.
%%sql
ALTER TABLE student DROP COLUMN email;

# 4. Naudokite PRAGMA table_info(student); ir patikrinkite atliktus pakeitimus.
%%sql
PRAGMA table_info(student);

# atspausdina istorija
history

# baigus darba atsijungti
exit