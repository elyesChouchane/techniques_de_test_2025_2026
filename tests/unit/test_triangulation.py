from triangulator.triangulation import triangulate

def test_3_points():
    pts = [(0.0, 0.0), (1.0, 0.0), (0.0, 1.0)]
    assert triangulate(pts) == [(0, 1, 2)]

def test_2_points():
    assert triangulate([(0,0), (1,1)]) == []

def test_empty():
    assert triangulate([]) == []

def test_colinear():
    pts = [(0,0), (1,1), (2,2)]
    assert triangulate(pts) == []