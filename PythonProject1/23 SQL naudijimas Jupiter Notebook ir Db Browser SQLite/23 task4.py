ipython

%load_ext sql
%sql sqlite:///cars.db

%config SqlMagic.style = '_DEPRECATED_DEFAULT'

 %sql SELECT * FROM cars;

# Grupavimas ir agregavimo funkcijos
# Dažniausiai naudojamos grupavimo funkcijos:
#
# AVG() – vidurkis
# COUNT() – eilučių skaičius
# MAX() – didžiausia reikšmė
# MIN() – mažiausia reikšmė
# SUM() – suma

%%sql
SELECT MIN(price), MAX(price), AVG(price) FROM cars;

%%sql
SELECT MIN(price), MAX(price), AVG(price) FROM cars;

# Automobilių kiekis pagal gamintoją:

%%sql
SELECT make, count(*) FROM cars GROUP BY make;


# Brangiausios spalvos pagal didžiausią kainą:

%%sql
SELECT color, max(price), make, model FROM cars GROUP BY color ORDER BY price DESC;

# atspausdina istorija
history

# baigus darba atsijungti
exit