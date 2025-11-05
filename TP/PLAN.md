# Plan de tests – Triangulator

## 1. Tests unitaires de la logique de triangulation
- Cas nominal : 3 points → 1 triangle
- Cas limite : 0, 1, 2 points → 0 triangle
- Points colinéaires → triangulation vide ou gérée
- Points en double → dédoublonnage ou gestion robuste

## 2. Tests de sérialisation binaire
- Encodage/décodage de PointSet (struct "I" + "ff")
- Encodage/décodage de Triangles (sommets + indices)
- Gestion des données tronquées ou corrompues

## 3. Tests de l’API HTTP (/triangulate)
- Réussite (200) avec PointSetID valide
- Erreur 404 si PointSetID inconnu
- Erreur 500 si PointSetManager injoignable
- Format de réponse binaire conforme

## 4. Tests de performance
- Temps de triangulation pour 10 / 100 / 1000 points
- Mesure via pytest + @pytest.mark.performance

## 5. Couverture
- Objectif : 100% avec `coverage`
- Tests pertinents, pas juste pour couvrir

## 6. Qualité du code
- Conformité à `ruff check`
- Documentation de toutes les fonctions (pour pdoc3)