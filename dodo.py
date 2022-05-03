from doit.tools import run_once


DOIT_CONFIG = {'default_tasks':
               ['docs', 'babel', 'private_settings', 'migrate', 'tests']}


def task_docs():
    """Creates documentation in html."""
    return {
        'actions': ['make -C ./docs html']
    }


def task_babel():
    """Creates generative files for babel (Translation)"""
    return {
        'actions': ['''cd CCwebsite/DeckBuilder/translation &&
        pybabel compile -D tools -d ./ -l ru &&
        pybabel compile -D tools -d ./ -l en &&
        pybabel compile -D tools -d ./ -l ru pybabel compile -D tools -d ./ -l ru''']
    }


def task_tests():
    """Run tests"""
    return {
        'actions': ['''cd CCwebsite && pytest ./tests/DeckBuilderTests.py''']
    }


def task_private_settings():
    """Generates default private_setting.json file."""
    return {
        'actions': ['''cd CCwebsite/CCwebsite && python3 generate_default_private_settings.py'''],
        'targets': ['./CCwebsite/CCwebsite/private_settings.json'],
        'uptodate': [run_once]
    }


def task_wheel():
    """Generates wheel distribution"""
    return {
        'actions': ['''python -m build -w'''],
        'task_dep': ["babel"]
    }


def task_migrate():
    """Create django databases"""
    return {
        'actions': ['''cd CCwebsite && python3 manage.py migrate''']
    }


def task_flake8():
    """Check for flake8"""
    return {
        'actions': ['flake8']
    }
