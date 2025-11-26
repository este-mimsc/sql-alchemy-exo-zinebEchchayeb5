# SQLAlchemy Flask Blog Assignment

**Étudiante**: Zineb Echchayeb  
**Repository**: [https://github.com/este-mimsc/sql-alchemy-exo-zinebEchchayeb5](https://github.com/este-mimsc/sql-alchemy-exo-zinebEchchayeb5)  
**Date**: Novembre 2025  

---

## Description

Ce projet est un exercice pratique pour apprendre à utiliser **Flask** avec **SQLAlchemy**.  
Il permet de créer une petite application de blog avec les fonctionnalités suivantes :

- Création et affichage des utilisateurs (`User`)  
- Création et affichage des posts (`Post`) liés à un utilisateur  
- Base de données SQLite pour le stockage  
- Gestion des migrations avec **Flask-Migrate**  

---

## Structure du projet
sql-alchemy-exo-zinebEchchayeb5/
├─ app/ # Contient le code principal de l'application
├─ migrations/ # Fichiers pour les migrations de la base de données
├─ tests/ # Tests unitaires
├─ instance/
├─ venv/ # Environnement virtuel
├─ blog.db # Base de données SQLite
├─ config.py # Configuration de Flask
├─ run.py # Script pour démarrer l'application
├─ requirements.txt # Dépendances Python
└─ README.md # Ce fichier


---

## Installation

1. Cloner le repository :  
```bash
git clone https://github.com/este-mimsc/sql-alchemy-exo-zinebEchchayeb5.git

python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate   # Linux / Mac
pip install -r requirements.txt
flask --app run.py run



