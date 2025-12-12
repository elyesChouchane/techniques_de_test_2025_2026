"""Core module containing the Triangulator component."""

class PointSetManager:
    """Interface simulée du gestionnaire de points (Database)."""

    def get_points(self, calculation_id: str) -> list:
        """Récupère les points associés à un ID.

        Dans la vraie vie, cela ferait une requête SQL/HTTP.
        Ici, on laisse vide car ce sera mocké.
        """
        raise NotImplementedError("Doit être mocké dans les tests.")


class Triangulator:
    """Composant principal responsable de la triangulation."""

    def __init__(self, manager: PointSetManager):
        """Injection de dépendance.

        Le Triangulator ne crée pas le manager, il le reçoit.
        Cela permet de remplacer le vrai manager par un Mock.
        """
        self.manager = manager

    def triangulate(self, calculation_id: str) -> tuple:
        """Orchestre le calcul pour un ID donné."""
        # 1. Interaction avec le PointSetManager
        points = self.manager.get_points(calculation_id)

        # 2. Gestion des erreurs (Scénario d'échec)
        if not points:
            raise ValueError(f"Aucun point trouvé pour l'ID {calculation_id}")

        if len(points) != 3:
            raise ValueError("La triangulation nécessite exactement 3 points.")

        # 3. Logique Métier (Le calcul)
        p1, p2, p3 = points

        # Vérification du format des données
        if not all(isinstance(p, tuple) and len(p) == 2 for p in [p1, p2, p3]):
            raise TypeError("Les points doivent être des tuples (x, y).")

        center_x = (p1[0] + p2[0] + p3[0]) / 3
        center_y = (p1[1] + p2[1] + p3[1]) / 3

        return (round(center_x, 2), round(center_y, 2))
