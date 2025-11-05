# Plan de tests – Triangulator

## 1. Tests unitaires de la logique de triangulation
- Cas nominal : 3 points -> 1 triangle (comportement attendu de base)
- Cas limite : 0, 1, 2 points -> 0 triangle (doit renvoyer une liste vide)
- Points colinéaires -> triangulation vide ou gérée
- Points en double -> dédoublonnage ou gestion robuste

## 2. Tests de sérialisation binaire
- Encodage/décodage de PointSet (struct "I" + "ff") (structure binaire exacte: 4 octets pour le nombre, puis paires de float)
- Encodage/décodage de Triangles (sommets + indices) (vérification de la double partie: sommets + indices de triangles)
- Gestion des données tronquées ou corrompues  (trop courtes ou mal formées pour éviter les crashs silencieux)

## 3. Tests de l’API HTTP (/triangulate)
- Réussite (200) avec PointSetID valide (réponse binaire conforme)
- Erreur 404 si PointSetID inconnu (n’existe pas dans le PointSetManager)
- Erreur 500 si PointSetManager injoignable (ex. : timeout)
- Format de réponse binaire conforme (corps binaire strictement conforme à la spécification Triangles)

## 4. Tests de performance
- Temps de triangulation pour 10 / 100 / 1000 points (identifier d’éventuels goulets d’étranglement)
- Mesure via pytest + @pytest.mark.performance

## 5. Couverture
- Objectif : 100% avec `coverage`
- Tests pertinents, pas juste pour couvrir (chaque test doit vérifier un comportement attendu avec des assertions précises)

## 6. Qualité du code
- Conformité à `ruff check` (respect du style, absence de code mort, etc)
- Documentation de toutes les fonctions (pour pdoc3)