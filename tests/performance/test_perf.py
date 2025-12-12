"""Tests de performance pour le Triangulator."""
import pytest
import time
from unittest.mock import Mock
from src.core import Triangulator

@pytest.mark.performance
def test_perf_100_triangulations():
    """Vérifie que 100 appels au composant sont rapides."""
    # 1. Setup : On crée un mock rapide qui renvoie toujours un triangle valide
    mock_manager = Mock()
    mock_manager.get_points.return_value = [(0, 0), (10, 0), (5, 10)]

    triangulator = Triangulator(manager=mock_manager)

    start_time = time.time()

    # 2. Exécution : 100 appels
    for i in range(100):
        # On utilise un ID fictif différent à chaque fois
        triangulator.triangulate(f"perf_id_{i}")

    duration = time.time() - start_time

    # 3. Validation : Moins de 1 seconde (c'est très large)
    assert duration < 1.0
