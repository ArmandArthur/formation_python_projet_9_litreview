# Litreview
Phrase de présentation du projet/programme.

- [Litreview](#litreview)
- [Cloner le dépôt du projet:](#cloner-le-dépôt-du-projet)
- [Aller sur le bon répertoire:](#aller-sur-le-bon-répertoire)
- [Installer l'environnement virtuel:](#installer-lenvironnement-virtuel)
- [Installer les dépendances et django:](#installer-les-dépendances-et-django)
- [Lancer le programme:](#lancer-le-programme)
- [Installer et run flake8:](#installer-et-run-flake8)

# Cloner le dépôt du projet:

`git clone git@github.com:ArmandArthur/formation_python_projet_9_litreview.git`
  
# Aller sur le bon répertoire:

`cd formation_python_projet_9_litreview`

# Installer l'environnement virtuel:

`python3 -m venv venv`<br />
`source ./venv/bin/activate` (UNIX)<br />
`./venv/scripts/activate` (windows)

# Installer les dépendances et django:

`pip install -r requirements.txt`

# Lancer le programme:

`cd src`<br />
`py manage.py runserver` (windows)<br />
`python3 manage.py runserver` (UNIX)

# Installer et run flake8:

`pip install flake8`<br />
`flake8 * > flake8_report.txt`


