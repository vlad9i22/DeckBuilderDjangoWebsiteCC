cd DeckBuilder/translation
pybabel compile -D tools -d ./ -l ru pybabel compile -D tools -d ./ -l en
pybabel compile -D tools -d ./ -l ru pybabel compile -D tools -d ./ -l ru
cd ../..
python3 manage.py runserver
