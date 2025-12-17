# Plan de Tests - Projet Triangulator

## 1. Objectifs
L'objectif est de valider le composant `Triangulator` de manière isolée, performante et robuste, en simulant ses dépendances externes.

## 2. Stratégie de Test

### A. Tests Unitaires (Isolation)
Nous utilisons `pytest` et `unittest.mock` pour isoler le composant.
- **Dépendance :** Le `PointSetManager` sera mocké (simulé).
- **Scénarios couverts :**
  - **Nominal :** Le manager renvoie 3 points valides -> Le calcul du barycentre est correct.
  - **Erreur de données :** Le manager renvoie une liste vide ou incomplète -> `ValueError`.
  - **Format invalide :** Les points ne sont pas des tuples conformes -> `TypeError`.

### B. Tests de Performance
Nous vérifions que le composant peut tenir la charge.
- **Scénario :** Exécution de 100 triangulations successives.
- **Critère d'acceptation :** Temps total < 1 seconde.

### C. Qualité de Code (Analyse Statique)
Utilisation de l'outil `ruff` pour garantir :
- Le respect de la PEP8.
- La présence de Docstrings sur tous les modules et fonctions.