"""Tests unitaires du Triangulator avec Mocking."""
import pytest
from unittest.mock import Mock
from src.core import Triangulator

def test_triangulation_success():
    """SCÉNARIO NOMINAL : Le manager renvoie bien 3 points."""
    # 1. ARRANGE : On prépare le Mock
    mock_manager = Mock()
    # Quand on appellera get_points, il renverra cette liste précise
    mock_manager.get_points.return_value = [(0, 0), (4, 0), (2, 4)]

    # On injecte le Mock dans le Triangulator
    triangulator = Triangulator(manager=mock_manager)

    # 2. ACT : On lance le calcul
    result = triangulator.triangulate("id_test_1")

    # 3. ASSERT : Vérifications
    # Vérifie le résultat mathématique
    assert result == (2.0, 1.33)
    # Vérifie que le Triangulator a bien "parlé" au manager avec le bon ID
    mock_manager.get_points.assert_called_once_with("id_test_1")


def test_triangulation_failure_not_enough_points():
    """SCÉNARIO D'ÉCHEC : Le manager renvoie seulement 2 points."""
    mock_manager = Mock()
    mock_manager.get_points.return_value = [(0, 0), (4, 0)]  # Pas assez de points

    triangulator = Triangulator(manager=mock_manager)

    # On vérifie que le code lève bien une erreur ValueError
    with pytest.raises(ValueError, match="exactement 3 points"):
        triangulator.triangulate("id_bad_data")


def test_triangulation_failure_no_data():
    """SCÉNARIO D'ÉCHEC : L'ID n'existe pas (liste vide)."""
    mock_manager = Mock()
    mock_manager.get_points.return_value = []  # Vide

    triangulator = Triangulator(manager=mock_manager)

    with pytest.raises(ValueError, match="Aucun point trouvé"):
        triangulator.triangulate("id_unknown")
