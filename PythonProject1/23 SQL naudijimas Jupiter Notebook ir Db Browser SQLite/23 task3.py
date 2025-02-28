
# 8. Teksto operacijos (||)
# Užduotis:
# Sukurkite naują stulpelį, kuris rodo mokytojo pilną vardą ir pavardę.
# %%sql
# SELECT vardas || ' ' || pavarde AS "Pilnas Vardas" FROM mokytojai;
# Sukurkite naują stulpelį "Dėsto", kuris rodo mokytojo dėstomą dalyką, pvz.:
# "Jonas Jonaitis dėsto Matematiką".

# Įkeliame SQL plėtinį ir prisijungiame prie duomenų bazės
ipython    #  enter

%load_ext sql
%sql sqlite:///mokykla.db


#pakeiciam konfiga kad graziau printintu
%config SqlMagic.style = '_DEPRECATED_DEFAULT'

# Atrenkame visus mokytojus
%%sql
SELECT * FROM mokytojai; # enter 2-3 kartus

#kad matyti value
%sql SELECT sql FROM sqlite_master WHERE type='table' AND name='mokytojai';

# Sukurti naują stulpelį su pilnu mokytojo vardu:

%%sql
SELECT vardas || ' ' || pavarde AS "Pilnas Vardas" FROM mokytojai;

# Sukurti naują stulpelį "Dėsto", kuris rodo mokytojo dėstomą dalyką:
%%sql
SELECT vardas || ' ' || pavarde || ' dėsto ' || dalykas AS "Dėsto" FROM mokytojai;




# 9. Matematiniai skaičiavimai
# Užduotis:
# Apskaičiuokite, kiek metų vidutiniškai dirba mokytojai, jei žinoma, kad vidutinis mokytojo
# darbo pradžios metai – 2005.
# %%sql
# SELECT 2024 - 2005 AS "Vidutinis patirties amžius";
# Apskaičiuokite atlyginimą be mokesčių (įvertinant, kad PVM 21%).
# %%sql
# SELECT vardas, pavarde, atlyginimas, ROUND(atlyginimas / 1.21, 2) AS
# "Be Mokesčių" FROM mokytojai;


# 3. Apskaičiuoti vidutinį mokytojų patirties laiką (darbo pradžios metai – 2005 m.):
%%sql
SELECT 2024 - 2005 AS "Vidutinis patirties amžius";

# Apskaičiuoti atlyginimą be PVM (kai PVM yra 21%):

%%sql
SELECT vardas, pavarde, atlyginimas, ROUND(atlyginimas / 1.21, 2) AS "Be Mokesčių" FROM mokytojai;

# atspausdina istorija
history

# baigus darba atsijungti
exit