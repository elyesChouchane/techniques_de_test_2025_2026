def triangulate(points):
    """Triangulation en éventail (fan). Ne fonctionne que si points[0] voit tous les autres."""
    n = len(points)
    if n < 3:
        return []
    # Vérifie colinéarité simple (optionnel, mais utile)
    if n == 3:
        x1, y1 = points[0]
        x2, y2 = points[1]
        x3, y3 = points[2]
        # Aire du triangle = 0 → colinéaire
        if abs((x2 - x1)*(y3 - y1) - (x3 - x1)*(y2 - y1)) < 1e-9:
            return []
    return [(0, i, i + 1) for i in range(1, n - 1)]