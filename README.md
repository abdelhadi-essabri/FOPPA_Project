<<<<<<< HEAD
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


# Visualiser les résultats

Pour visualiser les résultats de chaque partie, 2 moyens s'offre à vous:

- Exécuter les notebooks:
- Exécuter les scripts python

## Notebooks

Pour exécuter les notebooks, il faudra avoir installer **jupyter notebook**, 
par la suite lancer le à travers la commande ci-dessous, après avoir activé l'environnement au préalable:

```
jupyter notebook
```

De là il vous suffira d'exécuter le notebook que vous voulez

## Scripts python

Pour celà à partir de la racine du projet il suffira de faire:

```
python 01_exploration/lots.py
```

Cette commande affichera les résultats de l'exploration du lots


Les deux méthodes générerons des images pour les notebooks, elles y seront directement visible 
mais vous pourrez les consulter aussi en allant dans le répertoire **images**

Pour les scripts, vous ne pourrez les consulter qu'à partir du répertoire **images**

Les images de chaque parties sont précédées par le numéro de cette partie.



=======
# FOPPA_Project
>>>>>>> 5bbba429fd3e17d487c254fc9c8cc59c707a0942
