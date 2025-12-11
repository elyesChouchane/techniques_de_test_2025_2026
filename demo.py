from src.core import triangulate_points

print("--- DÉBUT DE LA DÉMO ---")

# Cas 1 : Triangle simple
p1 = (0, 0)
p2 = (4, 0)
p3 = (2, 4)
resultat = triangulate_points(p1, p2, p3)
print(f"Triangle {p1}, {p2}, {p3} -> Centre : {resultat}")

# Cas 2 : Triangle avec des négatifs
p1 = (-10, -10)
p2 = (10, -10)
p3 = (0, 10)
resultat = triangulate_points(p1, p2, p3)
print(f"Triangle {p1}, {p2}, {p3} -> Centre : {resultat}")

print("--- FIN ---")