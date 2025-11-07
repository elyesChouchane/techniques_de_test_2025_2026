"""Algorithme de triangulation simple en éventail (fan triangulation)."""


def triangulate(points):
    """Effectue une triangulation en éventail à partir d'une liste de points 2D.

    Fonctionne uniquement si le premier point peut "voir" tous les autres.
    Gère les cas dégénérés (moins de 3 points, colinéarité).

    Args:
        points: Liste de tuples (x, y) représentant les coordonnées.

    Returns:
        List[Tuple[int, int, int]]: Liste des triangles sous forme d'indices.
    """
    n = len(points)
    if n < 3:
        return []
    if n == 3:
        x1, y1 = points[0]
        x2, y2 = points[1]
        x3, y3 = points[2]
        # Calcul de l'aire signée du triangle
        if abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)) < 1e-9:
            return []
    return [(0, i, i + 1) for i in range(1, n - 1)]
