# Aufgabe 1

## Aufgabe 1.1

ODM bedeutet: Object Document Mapper
ODM ist ein Framework für die Verbindung zwischen Python und MongoDB.
ODM wandelt Python-Klassen in MongoDB-Dokumente um. Somit erleichtert das framework das bearbeiten der Datenbank.

## Aufgabe 1.2 (Output)

PS C:\Users\marvi\OneDrive - sluz\BBZW\M165 ELA\Mongo_Python> & "C:/Users/marvi/OneDrive - sluz/BBZW/M165
ELA/Mongo_Python/venv/Scripts/python.exe" "c:/Users/marvi/OneDrive - sluz/BBZW/M165 ELA/Mongo_Python/Aufgabe1.py"
{'version': '8.0.8', 'gitVersion': '7f52660c14217ed2c8d3240f823a2291a4fe6abd', 'modules': ['enterprise'], 'allocator': '
tcmalloc-google', 'javascriptEngine': 'mozjs', 'sysInfo': 'deprecated', 'versionArray': [8, 0, 8, 0], 'bits': 64, '
debug': False, 'maxBsonObjectSize': 16777216, 'storageEngines': ['devnull', 'inMemory', 'queryable_wt', 'wiredTiger'], '
ok': 1.0, '$clusterTime': {'clusterTime': Timestamp(1746782735, 52), 'signature': {'hash': b"
\xe0\xffO\xb7\x94g\xabD\xd1\xe1H'\xcf7\xc6\x1d\xa8\xc7\x08d", 'keyId': 7461309390969110556}}, 'operationTime':
Timestamp(1746782735, 52)}
airb
airb2
media
music
my_database
social_media
admin
local
Database exists.

# Aufgabe 2 (Output)

Databases

- airb
- db_restaurants
- sample_mflix
- admin
- local

Select Database: airb

airb

Collections

- listingsAndReviews

Select Collection: listingsAndReviews

airb.listingsAndReviews

Documents

- 10082307
- 10082422
- ...
- 9795621
- 9846545
- 9895628
- 9907103
- 67f8dbd03fcac5e13acb0ce2

Select Document: 67f8dbd03fcac5e13acb0ce2

airb.listingsAndReviews.67f8dbd03fcac5e13acb0ce2

name: Yannicks Unterkunft
property_type: Apartment
bed_type: Full Bed
bathrooms: 1.0
amenities: ['Wifi', 'Kitchen', 'Heating', 'Essentials']
price: 95.00
host: {'host_name': 'Yannick Blatty'}
address: {'street': 'St, Antonstrasse 7', 'country': 'Switzerland', 'country_code': 'CH'}

Press any button to return


# Aufgabe 3

## Aufgabe 3.1 (Output)
Bronx
Brooklyn
Manhattan
Missing
Queens
Staten Island


## Aufgabe 3.2 (Output)
Juice It Health Bar, score: 75.00
Golden Dragon Cuisine, score: 73.00
Palombo Pastry Shop, score: 69.00


## Aufgabe 3.3 (Output)
Subway, [-73.96511939999999, 40.75532949999999]

## Aufgabe 3.4 (Output)
Name (optional): Steak
Küche (optional): Italian
 Bistecca Fiorentina Steak, Küche:Italian
 5 Star Cheesesteak And Pizza, Küche:Pizza/Italian
 Quality Italian Steakhouse, Küche:Italian
 Tommys Famous Cheesesteaks & Pizza, Küche:Pizza/Italian
 Davio'S Northern Italian Steakhouse, Küche:Italian

## Aufgabe 3.5 (Output)
 Name (optional): Steak
Küche (optional): Italian
1. Bistecca Fiorentina Steak, Küche: Italian
2. 5 Star Cheesesteak And Pizza, Küche: Pizza/Italian
3. Quality Italian Steakhouse, Küche: Italian
4. Tommys Famous Cheesesteaks & Pizza, Küche: Pizza/Italian
5. Davio'S Northern Italian Steakhouse, Küche: Italian
Restaurant für Bewertung auswählen: 1
Bewertung: A
Bewertung gespiechert