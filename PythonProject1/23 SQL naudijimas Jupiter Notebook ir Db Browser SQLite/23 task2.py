# Užduotis

# 5. Rikiavimas (ORDER BY)
# Užduotis:
# Išrikiuokite mokytojus pagal atlyginimą mažėjančia tvarka.
# Išrikiuokite mokytojus pagal pavardę abėcėlės tvarka.
# %%sql
# SELECT * FROM mokytojai ORDER BY atlyginimas DESC;
# Išrikiuokite mokytojus pagal dalyką, o jei dalykai sutampa – pagal atlyginimą (didėjančia
# tvarka).



# 6. Kombinuotos užklausos (AND, OR, NOT)
# Užduotis:
# Atrinkite visus mokytojus, kurie dėsto "Matematiką" ir gauna daugiau nei 2000 atlyginimą.
# Atrinkite visus mokytojus, kurie dėsto "Fiziką" arba "Chemiją".
# %%sql
# SELECT * FROM mokytojai WHERE dalykas = 'Matematika' AND atlyginimas >
# 2000;
# Atrinkite mokytojus, kurie nedėsto "Lietuvių" ir "Istorijos".

# Parasyti
# ipython      enter

# atsiranda zalios spalvos  In [1]:

# Sukuriame arba prisijungiame prie duombazes
%load_ext sql    enter
%sql sqlite:///mokykla.db    enter

# po kiekvienos komandos spausti 2-3 kartus enter kad isirasytu duomenys

#pakeiciam konfiga kad graziau printintu
%config SqlMagic.style = '_DEPRECATED_DEFAULT'

#kad matyti value
%sql SELECT sql FROM sqlite_master WHERE type='table' AND name='mokytojai';

# atvaizduoja mokytojus
%%sql
SELECT * FROM mokytojai;

# Mokytojų rikiavimas pagal atlyginimą mažėjančia tvarka:
%%sql
SELECT * FROM mokytojai ORDER BY atlyginimas DESC;

# Mokytojų rikiavimas pagal pavardę abėcėlės tvarka:
%%sql
SELECT * FROM mokytojai ORDER BY pavarde ASC;

# Mokytojų rikiavimas pagal dalyką, o jei dalykai sutampa – pagal atlyginimą didėjančia tvarka
%%sql
SELECT * FROM mokytojai ORDER BY dalykas ASC, atlyginimas ASC;

# Atrinkti visus mokytojus, kurie dėsto "Matematiką" ir gauna daugiau nei 2000 atlyginimą:
%%sql
SELECT * FROM mokytojai WHERE dalykas = 'Matematika' AND atlyginimas > 2000;

# Atrinkti visus mokytojus, kurie dėsto "Fiziką" arba "Chemiją":
%%sql
SELECT * FROM mokytojai WHERE dalykas = 'Fizika' OR dalykas = 'Chemija';


# Atrinkti mokytojus, kurie nedėsto "Lietuvių" ir "Istorijos":
%%sql
SELECT * FROM mokytojai WHERE dalykas NOT IN ('Lietuvių', 'Istorija');

# atspausdina istorija
history

#baigus darba atsijungti
exit