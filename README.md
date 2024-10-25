
# Marchés Publics et Base FOPPA

## Description
Ce projet vise à explorer, nettoyer et analyser des données issues de marchés publics en France dans le cadre du projet DeCoMaP (Détection de la Corruption dans les Marchés Publics), financé par l'Agence Nationale de la Recherche (ANR) et réalisé avec l'Université d'Avignon. L'objectif est de développer des méthodes pour détecter des schémas de fraude et fournir une analyse descriptive complète des données disponibles.  
Les données utilisées proviennent de la base FOPPA (French Open Public Procurement Award notices), contenant des informations sur les appels d'offres et les attributions de marchés pour la période 2010-2020.

## Membres de l'équipe
Le projet a été mené par l'équipe "FraudeScan" (Groupe 07) :
- **Abdelhadi Essabri** (M2 IA)
- **Bouchra El Houari** (M2 ILSEN)
- **Michel Marie Lamah** (M2 IA)

**Responsable** : Vincent Labatut, Responsable académique, Université d'Avignon

---

# Guide d'installation et configuration

Ce guide vous aide à installer l'environnement nécessaire et les dépendances pour exécuter le code.

### Étape 1: Créer un environnement
Pour créer un environnement virtuel nommé "foppa" en utilisant conda :
```bash
conda create --name foppa python=3.9
```

### Étape 2: Installer les packages
Activez l'environnement et installez les packages requis depuis `requirements.txt` :
```bash
conda activate foppa
pip install -r requirements.txt
```

### Étape 3: Installer les modules localement
Pour rendre les modules disponibles partout :
```bash
pip install -e .
```

Assurez-vous d'exécuter cette commande dans le répertoire racine du projet contenant le fichier `setup.py`.

---

## Structure du répertoire
Le projet est organisé en plusieurs répertoires dédiés :
- **01_exploration** : Scripts pour l'exploration des données.
- **02_nettoyage** : Scripts pour le nettoyage des données.
- **03_analyse_descriptive** : Scripts pour l'analyse descriptive.
- **04_questionnements** : Scripts pour le questionnement et l'analyse exploratoire.
- **05_extension** : Scripts pour l'extension des données.
- **05_graphe** : Scripts pour l'analyse par graphes.

## Technologies et Bibliothèques
Les bibliothèques utilisées incluent :
- **Pandas** : Manipulation et analyse des données.
- **Matplotlib** : Création de visualisations.
- **Scikit-learn** : Prétraitement des données et clustering.
- **NetworkX** : Analyse et visualisation des graphes.
- **Community** : Détection de communautés dans les graphes.

---

# Utilisation et exécution

Les scripts peuvent être exécutés dans l'ordre des répertoires pour reproduire l'analyse.

### Exécuter avec Jupyter Notebook
Pour utiliser les notebooks :
1. Installez **Jupyter Notebook**.
2. Lancez avec la commande :
   ```bash
   jupyter notebook
   ```
3. Exécutez le notebook souhaité.

### Exécuter les scripts Python
À partir de la racine du projet :
```bash
python 01_exploration/lots.py
```

### Visualisation des résultats
Les deux méthodes génèrent des images qui seront visibles directement dans les notebooks ou dans le répertoire **images**. Les fichiers image sont nommés selon le numéro de chaque partie.

---

## Contributions de l'équipe
- **Abdelhadi Essabri** : Analyse des tables Agents, Names, LotBuyers, LotSuppliers.
- **Bouchra El Houari** : Analyse de la table Criteria.
- **Michel Marie Lamah** : Analyse des Lots et génération des graphiques.

## Résultats
L'analyse a permis d'extraire des informations sur les pratiques de marché, les schémas d'attribution, et la part des PME dans les marchés publics. Une partie de l'analyse s'est concentrée sur la détection de similitudes entre les lots et les agents avec des algorithmes de clustering et de détection d'anomalies.

