import json


if __name__ == '__main__':
    SITE_ID = 3
    SECRET_KEY = "django-insecure-t@gn&u$f6(npvsf!v#uhy7%#e_kak**ki^(-%)oxzk%piscbw9"
    private_settings = {
        "SITE_ID": SITE_ID,
        "SECRET_KEY": SECRET_KEY
    }
    with open('private_settings.json', 'w') as f:
        json.dump(private_settings, f)
