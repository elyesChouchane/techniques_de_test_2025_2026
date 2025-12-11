"""Core module for triangulation logic."""

def triangulate_points(p1: tuple, p2: tuple, p3: tuple) -> tuple:
    
    # Validation basique pour éviter des erreurs silencieuses
    if not all(isinstance(p, tuple) and len(p) == 2 for p in [p1, p2, p3]):
        raise TypeError("All points must be tuples of (x, y) coordinates.")

    # Calcul de la moyenne des X et de la moyenne des Y
    center_x = (p1[0] + p2[0] + p3[0]) / 3
    center_y = (p1[1] + p2[1] + p3[1]) / 3
    
    print(f"DEBUG: Points {p1}, {p2}, {p3} -> Centre ({center_x}, {center_y})")
    return (round(center_x, 2), round(center_y, 2))
