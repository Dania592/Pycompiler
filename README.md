# Pycompiler

Pycompiler est un compilateur écrit en Python pour un langage simplifié inspiré du C.  
Il a été réalisé dans le cadre du module de compilation (APP4) en informatique et ingénierie mathématique.

---

## Lancement

- Fichier principal : `CompilateurC.py`  
- Exécution : `python CompilateurC.py fichier_a_compiler.c`  
- La sortie correspond au code assembleur généré, affiché dans le terminal.

Pour exécuter le code produit, il suffit de rediriger la sortie vers un fichier puis de l’utiliser avec le simulateur.

---

## Fonctionnement du compilateur

### Analyse lexicale
Identifie les tokens présents dans le fichier source et les renvoie un par un.

### Analyse syntaxique
Parcourt la liste des tokens, construit l’arbre syntaxique (AST) et vérifie la validité du programme.

### Analyse sémantique / Génération de code
Produit le code assembleur correspondant à l’arbre syntaxique généré.

---

## Structure du projet

- **CompilateurC.py** : fichier principal qui coordonne l’ensemble du processus.  
- **Object.py** : contient les classes `Token` et `Node` utilisées pour la représentation interne du programme.  
- **config.py** : regroupe les variables globales, règles de syntaxe et dictionnaires utilisés par les analyseurs.

---
