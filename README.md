# Django-harjoitus 2023 tammi-maaliskuu
Django harjoittelua alkuvuodesta 2023


## Asennus
1. Tee Python-virtuaaliympäristö
   ```
   python -m venv venv
   ```
2. Aktivoi virtuaaliympäristö
   - Voit tehdä tämän VSCodessa, joko vastaamalla Yes kun VSCode kysyy että aktivoidaanko virtuaaliympäristö tai jos tätä kysymystä ei
   tule, niin klikkaamalla versionumeroa Python-sanan vierestä
   alapalkista. Python-sana tulee alapalkkiin, kun avaat jonkin
   py-tiedoston (esim. manage.py).
    - Voit myös aktivoida virtuaaliympäristön komentoriviltä
    ```
    venv/scripts/activate.ps1
    ```
3. Asenna tarvittavat Python-paketit
    ```
    pip install -r requirements.txt
    ```
4. Aja migraatiot tietokantaan:
    ```
    python manage.py migrate
    ```
    - Tämä luo SQLite-tietokannan
    'db.sqlite3'-tiedostoon
5. Luo pääkäyttäjä:
    ```
    python manage.py createsuperuser
    ```

## Kehitysympäristön käynnistäminen

Aja Djangon runserver komento:
```
python manage.py runserver
```

## Uusien migraatiotiedostojen tekeminen

Kun teet muutoksia models.py-tiedostoon, niin model-muutokset pitää saada myös tietokantaan. Tähän käytetään migraatiotiedostoja. Tehtyjen muutosten pohjalta voi luoda uuden migraatiotiedoston komennolla:
```
python manage.py makemigrations
```
