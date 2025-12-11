"""Tests de performance de la triangulation."""
import pytest
import random
import time
from src.core import triangulate_points  # <--- Correction de l'import


@pytest.mark.performance
def test_perf_100_triangles():
    """Mesure le temps de calcul pour 100 triangulations successives."""
    # Génération de 300 points aléatoires (pour faire 100 triangles de 3 points)
    points = [(random.random(), random.random()) for _ in range(300)]

    start = time.time()

    # On boucle 100 fois pour trianguler des groupes de 3 points
    for i in range(0, 300, 3):
        p1 = points[i]
        p2 = points[i+1]
        p3 = points[i+2]
        triangulate_points(p1, p2, p3)

    duration = time.time() - start
    
    # Vérification que les 100 calculs prennent moins d'une seconde
    assert duration < 1.0