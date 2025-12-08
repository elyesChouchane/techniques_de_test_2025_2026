# Retour d'Expérience - Triangulator

## Bilan
Le projet est terminé et fonctionnel. Tous les tests passent (Unitaires et Intégration) avec une couverture de 98%.

## Analyse du Plan initial vs Réalité
* **Réussite :** La structure découpée (Serializer / Core / App) définie dans le `PLAN.md` a été respectée. Cela a rendu les tests unitaires très simples à écrire.
* **Évolution :** J'avais sous-estimé la complexité de tester Flask. J'ai dû apprendre à utiliser les "fixtures" Pytest et `requests-mock` pour simuler le `PointSetManager` sans avoir besoin de lancer deux serveurs en parallèle.

## Difficultés Techniques
La principale difficulté fut la gestion du format binaire (`struct`).
* *Problème :* Au début, mes tests échouaient car j'utilisais le format natif Python pour les entiers, ce qui variait selon la machine.
* *Solution :* J'ai forcé le Little Endian (`<`) et le type `I` (4 bytes) pour garantir la compatibilité avec la spécification.

## Améliorations Possibles
L'algorithme de triangulation est un "Fan" basique. Il fonctionne bien pour les formes convexes mais peut créer des artefacts sur des formes très concaves. Une implémentation de "Ear Clipping" serait plus robuste pour une V2.