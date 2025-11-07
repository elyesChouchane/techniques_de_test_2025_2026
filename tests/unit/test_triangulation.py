"""Tests unitaires pour l'algorithme de triangulation."""

from triangulator.triangulation import triangulate


def test_3_points():
    """Test avec 3 points non colinéaires → 1 triangle."""
    pts = [(0.0, 0.0), (1.0, 0.0), (0.0, 1.0)]
    assert triangulate(pts) == [(0, 1, 2)]


def test_2_points():
    """Moins de 3 points → aucune triangulation."""
    assert triangulate([(0, 0), (1, 1)]) == []


def test_empty():
    """Liste vide → aucune triangulation."""
    assert triangulate([]) == []


def test_colinear():
    """Points colinéaires → aucune triangulation."""
    pts = [(0, 0), (1, 1), (2, 2)]
    assert triangulate(pts) == []
