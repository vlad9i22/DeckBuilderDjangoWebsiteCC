*Setting up after git clone.*
==================================
**Create and activate empty enviroment in the git cloned directory**

``python3 -m venv venv``

``source ./venv/bin/activate``

**Install requierments**

``pip install -r requirements.txt``

**Create all required files with DoIt**

``doit``


Running released version
=========================

**Download \*.whl realeased version** of website from https://github.com/vlad9i22/DeckBuilderDjangoWebsiteCC/tags.

**Setup requierments and wheel unpack**

``pip install name_of_downloaded_file.whl``

``wheel unpack name_of_downloaded_file.whl``

**Create required databases**

Go to the CCwebsite directory and run:
``python3 manage.py migrate``


Running server
==================

Go to CCwebsite directory and run:

``python3 manage.py runserver``

**Note that you should change private keys in order to run server in production**
