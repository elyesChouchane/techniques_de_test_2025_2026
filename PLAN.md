# Plan de Tests - Micro-service Triangulator

## 1. Introduction
Ce document décrit la stratégie de test pour le développement du micro-service `Triangulator`.
Ce composant a pour responsabilité de récupérer des ensembles de points (PointSet) via une API externe, de calculer leur triangulation, et de renvoyer le résultat sous un format binaire strict.

**Enjeux critiques :**
* Respect rigoureux du protocole binaire (Little Endian, float 32-bit).
* Indépendance vis-à-vis du service tiers `PointSetManager` (nécessité de Mocking).
* Robustesse de l'algorithme de triangulation.

## 2. Environnement et Outillage
* **Langage :** Python 3.10+
* **Serveur Web :** Flask
* **Framework de Test :** `pytest`
* **Mocking HTTP :** `requests-mock` (pour simuler le PointSetManager)
* **Analyse de Qualité :** `ruff` (linter) et `coverage` (couverture de code)
* **Documentation :** `pdoc3`

## 3. Stratégie de Test

Nous adopterons une approche "Test First" divisée en trois niveaux :

### 3.1. Tests Unitaires (Logique Pure)
Ces tests valideront les modules internes sans démarrer le serveur Flask ni effectuer d'appels réseau.

* **Module de Sérialisation (`serializer.py`) :**
    * *Test 1 (Nominal) :* Conversion `List[Point] -> bytes` et vérification de la taille en octets (Header + Payload).
    * *Test 2 (Nominal) :* Conversion inverse `bytes -> List[Point]` et vérification de l'intégrité des float.
    * *Test 3 (Erreur) :* Injection de données binaires corrompues ou tronquées (doit lever `ValueError`).
    
* **Module de Calcul (`core.py`) :**
    * *Test 1 (Triangle) :* 3 points → 1 triangle retourné.
    * *Test 2 (Carré) :* 4 points → 2 triangles retournés.
    * *Test 3 (Limites) :* Moins de 3 points → Retourne une liste vide (pas de crash).

### 3.2. Tests d'Intégration (API & Mocking)
Ces tests valideront le comportement du serveur Flask et de ses endpoints. Le service externe `PointSetManager` sera systématiquement "mocké" pour garantir la stabilité des tests.

* **Endpoint `GET /triangulation/<id>` :**
    * *Scénario Nominal :* 1. Le Mock simule une réponse 200 avec un binaire valide.
        2. Le `Triangulator` renvoie 200 et un binaire `Triangles` valide.
    * *Scénario "Introuvable" :* 1. Le Mock simule une réponse 404 (ID inconnu).
        2. Le `Triangulator` doit propager l'erreur (404).
    * *Scénario "Crash Externe" :* 1. Le Mock simule une erreur 500 ou un Timeout.
        2. Le `Triangulator` doit gérer l'erreur proprement (502/503).

### 3.3. Tests de Performance
Une suite de tests spécifique (marquée `@pytest.mark.perf`) sera mise en place pour vérifier le comportement sous charge.
* **Objectif :** Mesurer le temps de triangulation pour un nuage de 10 000 points.
* **Condition :** Le test échouera si le temps d'exécution dépasse un seuil défini (ex: 2 secondes).

## 4. Organisation du Projet
L'architecture séparera clairement la logique métier de l'interface HTTP pour faciliter les tests unitaires :
```text
src/
 ├── serializer.py  # Testable unitairement (struct pack/unpack)
 ├── core.py        # Testable unitairement (algo pur)
 └── app.py         # Testable via Tests d'Intégration