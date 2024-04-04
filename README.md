# Guide d'installation

Ce guide vous aidera à mettre en place l'environnement nécessaire et à installer les dépendances pour faire fonctionner le code.

## Étape 1: Création d'un environnement

Pour créer un environnement virtuel nommé "foppa" en utilisant conda, exécutez la commande suivante dans votre terminal :

```
conda create --name foppa python=3.9
```


## Étape 2: Installation des packages

Une fois que l'environnement est créé, activez-le en utilisant la commande suivante :

```
conda activate foppa
```

Ensuite, installez les packages requis à partir du fichier requirements.txt en utilisant la commande suivante :

```
pip install -r requirements.txt
```


Assurez-vous que vous êtes dans le répertoire contenant le fichier requirements.txt avant d'exécuter cette commande.

## Étape 3: Rendre les modules disponibles partout

Pour rendre les modules disponibles partout, vous pouvez installer le package localement en mode éditable en utilisant la commande suivante :

```
pip install -e .
```


Assurez-vous d'exécuter cette commande dans le répertoire racine du projet où se trouve le fichier setup.py.

C'est tout ! Vous avez maintenant configuré l'environnement et installé les dépendances nécessaires pour faire fonctionner le code.





