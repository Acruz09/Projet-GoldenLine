# Projet GoldenLine

## Table des matières
- [Description](#description)
- [Installation](#%EF%B8%8F-installation)
- [Utilisation](#utilisation)
- [Auteur](#-auteur)


## Description
Application web avec l'utilsation du framework Django destinée à GoldenLine pour la visualisation de statistiques de sa clientèle.



## 🛠️ Installation
0. Installer Git (si pas déja fait) en le téléchargement depuis le site officiel :
```bash
https://git-scm.com/downloads 
```
1. Clonage du référenciel :
```bash
git clone https://github.com/Acruz09/Projet-GoldenLine.git
```
2. Accéder au répertoire du projet :
```bash
cd '.\Projet-GoldenLine\Application web\' 
```
3. Activer l'environnement virtuel :
(pour Windows) :
```bash
.\env_goldenline\Scripts\activate
```
(pour MacOS et Linux) :
```bash
source env_goldenline/bin/activate
```
4. Installer les dépendances :
```bash
pip install -r requirements.txt
```
5. Lancer le projet
```bash
py manage.py runserver
```
        
## Utilisation
Se rendre sur le site de l'application web en suivant le lien :
[Application web](https://acruz19.pythonanywhere.com/).

S'authentifié en utilisant vos identifians de connexion.

La présentation de la page d'acceuil dépend des permissions que votre compte :
- Analyse : peut voir les données statistiques.
- Export : peut exporter les données de la base de données.
- Administrateur : possède les toutes les permission, peut ajouter un utilisateurs et definir ses permission, modifier les permissions des utilisateurs existants, voir la liste des utilisateurs.

## Tests de l'application
Des tests de l'application peuvent être effectuées depuis le terminal avec la ligne de commande :
```bash
coverage run .\manage.py test
```
Pour voir le rapport des tests : 
```bash
coverage html
```

## 🙇 Auteur
#### Danglades Yohann
- Github: [@acruz09](https://github.com/Acruz09)
