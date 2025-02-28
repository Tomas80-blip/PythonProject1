# 1. Mokytojų atlyginimų analizė
# • Suskaičiuokite, kiek yra mokytojų kiekviename dalyke.
# • Atrinkite dalykus, kuriuose dirba daugiau nei 3 mokytojai.
# • Suskaičiuokite vidutinį atlyginimą kiekviename dalyke ir atrinkite tuos, kur vidurkis
# viršija 2500.

ipython

%load_ext sql
%sql sqlite:///mokykla.db


#pakeiciam konfiga kad graziau printintu
%config SqlMagic.style = '_DEPRECATED_DEFAULT'

# Atrenkame visus mokytojus
%%sql
SELECT * FROM mokytojai; # enter 2-3 kartus

#kad matyti value
%sql SELECT sql FROM sqlite_master WHERE type='table' AND name='mokytojai';


# Suskaičiuokite, kiek yra mokytojų kiekviename dalyke.

%%sql
SELECT dalykas, COUNT(*) AS mokytoju_skaicius
FROM mokytojai
GROUP BY dalykas;

# Atrinkite dalykus, kuriuose dirba daugiau nei 3 mokytojai.


%%sql
SELECT dalykas, COUNT(*) AS mokytoju_skaicius
FROM mokytojai
GROUP BY dalykas
HAVING COUNT(*) > 3;

# Suskaičiuokite vidutinį atlyginimą kiekviename dalyke ir atrinkite tuos, kur vidurkis
# viršija 1500.

%%sql
SELECT dalykas, AVG(atlyginimas) AS vid_atlyginimas
FROM mokytojai
GROUP BY dalykas
HAVING AVG(atlyginimas) > 1500;


exit


# 2. Brangiausių automobilių analizė
# • Atrinkite brangiausią kiekvieno gamintojo automobilį.
# • Suskaičiuokite vidutinę automobilių kainą kiekvienam gamintojui ir atrinkite tik
# tuos, kurių vidutinė kaina viršija 40 000.
# • Suskaičiuokite, kiek skirtingų spalvų turi kiekvienas gamintojas ir išrikiuokite pagal
# spalvų kiekį mažėjančia tvarka.

ipython

%load_ext sql
%sql sqlite:///cars.db

%config SqlMagic.style = '_DEPRECATED_DEFAULT'

 %sql SELECT * FROM cars;

# • Atrinkite brangiausią kiekvieno gamintojo automobilį.

%%sql
SELECT make, model, year, MAX(price) AS max_price
FROM cars
GROUP BY make
ORDER BY max_price DESC;

# • Suskaičiuokite vidutinę automobilių kainą kiekvienam gamintojui ir atrinkite tik
# tuos, kurių vidutinė kaina viršija 40 000.

%%sql
SELECT make, AVG(price) AS avg_price
FROM cars
GROUP BY make
HAVING avg_price > 40000
ORDER BY avg_price DESC;

# • Suskaičiuokite, kiek skirtingų spalvų turi kiekvienas gamintojas ir išrikiuokite pagal
# spalvų kiekį mažėjančia tvarka.

%%sql
SELECT make, COUNT(DISTINCT color) AS color_count
FROM cars
GROUP BY make
ORDER BY color_count DESC;

# atspausdina istorija
history

# baigus darba atsijungti
exit