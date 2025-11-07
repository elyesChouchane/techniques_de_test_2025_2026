"""Tests de performance de la triangulation."""

import pytest
import random
from triangulator.triangulation import triangulate


@pytest.mark.performance
def test_perf_100_points():
    """Mesure le temps de triangulation pour 100 points."""
    pts = [(random.random(), random.random()) for _ in range(100)]
    import time
    start = time.time()
    triangulate(pts)
    assert time.time() - start < 1.0  # Moins d'une seconde
