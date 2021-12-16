# Installer le projet 
### Créer un environnement virtuel python et excuter 
- Ce projet à été écrit en python 3.7.10
- Avant être sur de bien avoir tkinter `sudo apt-get install python3-tk`
- Créer un environnement virtuel avec **venv** nommé "venv"  
`python3 -m venv venv`
- Démarrer l'environnement virtuel "venv"  
`source venv/bin/activate`
- Installer les modules python avec le fichier _requirement_.txt  
`pip install -r requirements.txt`
- Démarrer le projet `python mvc.py`


# Configurer le moteur
Le moteur d'inférence à été codé dans le fichier *inference.py* il est serait tout à fait possible
d'utiliser le moteur pour d'autres application ici nous avons décider de prendre **la reconnaissance de forme géométrique**
comme notre domaine d'application
# les règles
Nous pouvons avons choisi comme langage de régle un sous ensemble de
python, répresenter par des fonction booléenne nous pouvons définir 
un ensemble de régle et de méta régle dans le fichier *rules.py*

# l'interface graphique 
Nous pouvons dessiner une forme dans le canvans dédié est choisir le
type de chainage que nous shouaitons éxecuter.
Il est possible depuis l'interface : 
- De demander à activer les trace détaillé ou non dans le terminal.
- D'activer les méta-régles définie dans le fichier *rules.py* (Cela permet de rendre compte de l'efficasité des méta régles)



