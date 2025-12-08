"""
Cœur logique de la triangulation.
"""

def triangulate_points(points: list[tuple[float, float]]) -> list[tuple[int, int, int]]:
    """
    Réalise une triangulation simple (Fan Triangulation).
    Trie les points par coordonnée X pour éviter les croisements évidents.
    """
    if len(points) < 3:
        return []

    # On trie les indices des points en fonction de leur coordonnée X (puis Y)
    # Cela permet de "dérouler" le polygone plus proprement.
    sorted_indices = sorted(range(len(points)), key=lambda k: points[k])

    triangles = []
    pivot = sorted_indices[0]  # Le point le plus à gauche

    # On relie le pivot à tous les segments suivants
    for i in range(1, len(sorted_indices) - 1):
        idx_a = sorted_indices[i]
        idx_b = sorted_indices[i + 1]
        triangles.append((pivot, idx_a, idx_b))

    return triangles