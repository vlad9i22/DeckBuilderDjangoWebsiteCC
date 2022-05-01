DOIT_CONFIG = {'default_tasks':
               ['docs', 'babel', 'tests', 'migrate']}


def task_docs():
    return {
        'actions': ['make -C ./docs html']
    }


def task_babel():
    return {
        'actions': ['''cd CCwebsite/DeckBuilder/translation &&
        pybabel compile -D tools -d ./ -l ru &&
        pybabel compile -D tools -d ./ -l en &&
        pybabel compile -D tools -d ./ -l ru pybabel compile -D tools -d ./ -l ru''']
    }


def task_tests():
    return {
        'actions': ['''cd CCwebsite && pytest ./tests/DeckBuilderTests.py''']
    }


def task_generate_default_private_config():
    return {
        'actions': ['''cd CCwebsite/CCwebsite && python3 generate_default_private_settings.py'''],
        'targets': ['private_settings.json']
    }


def task_migrate():
    return {
        'actions': ['''cd CCwebsite && python3 manage.py migrate''']
    }


def task_flake8():
    return {
        'actions': ['flake8']
    }
