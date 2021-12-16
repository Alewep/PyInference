# Installer le projet 
### Créer un environnement virtuel python et exécuter 
- Ce projet a été écrit en python 3.7.10
- Avant être sûr de bien avoir tkinter `sudo apt-get install python3-tk`
- Créer un environnement virtuel avec **venv** nommé "venv"  
`python3 -m venv venv`
- Démarrer l'environnement virtuel "venv"  
`source venv/bin/activate`
- Installer les modules python avec le fichier _requirement_.txt  
`pip install -r requirements.txt`
- Démarrer le projet `python mvc.py`


# Configurer le moteur
Le moteur d'inférence a été codé dans le fichier *inference.py* il serait tout à fait possible
d'utiliser le moteur pour d'autres applications ici nous avons décidé de prendre **la reconnaissance de forme géométrique**
comme notre domaine d'application.
# les règles
Nous avons choisi comme langage de règle un sous-ensemble de
python, répresenté par des fonction booléenne nous pouvons définir 
un ensemble de régle et de méta règle dans le fichier *rules.py*

format d'une règle : `declare_rule(lambda expr,{"x":1,"y":2})`


# l'interface graphique 
Nous pouvons dessiner une forme dans le canvans dédié et choisir le
type de chainage que nous souhaitons éxecuter.
Il est possible depuis l'interface : 
- De demander a activer les traces détaillées ou non dans le terminal.
- D'activer les méta-régles définies dans le fichier *rules.py* (Cela permet de rendre compte de l'efficacité des méta-régles)



