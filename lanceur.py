# lanceur.py
import subprocess

# Définir les commandes à exécuter
commands = [
    # "git clone https://github.com/BurhanMohammad/Django-portfilio-website.git",
    # "cd Django-portfilio-website",
    "python manage.py makemigrations",
    "python manage.py migrate",
    "python manage.py runserver"
]

# Exécuter chaque commande
for command in commands:
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    process.wait()
    print(process.stdout.read().decode())