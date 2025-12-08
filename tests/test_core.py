from src.core import triangulate_points


def test_triangulation_triangle():
    """3 points forment 1 triangle."""
    points = [(0,0), (1,0), (0,1)]
    tris = triangulate_points(points)
    assert len(tris) == 1

def test_triangulation_square():
    """4 points forment 2 triangles."""
    points = [(0,0), (1,0), (0,1), (1,1)]
    tris = triangulate_points(points)
    assert len(tris) == 2

def test_not_enough_points():
    assert triangulate_points([(0,0)]) == []