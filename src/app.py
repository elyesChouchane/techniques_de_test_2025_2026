"""
Point d'entrée de l'application Flask.
"""
import os

import requests
from flask import Flask, Response

from src.core import triangulate_points
from src.serializer import bytes_to_point_set, triangles_to_bytes

app = Flask(__name__)

# Configuration de l'URL du service tiers (avec valeur par défaut)
MANAGER_URL = os.environ.get("POINT_SET_MANAGER_URL", "http://point_set_manager:5000")

@app.route('/triangulation/<point_set_id>', methods=['GET'])
def triangulate(point_set_id):
    """
    Endpoint principal.
    1. Récupère le PointSet via HTTP.
    2. Calcule la triangulation.
    3. Renvoie le résultat en binaire.
    """
    try:
        # Appel au PointSetManager
        resp = requests.get(f"{MANAGER_URL}/point_sets/{point_set_id}", timeout=5)

        if resp.status_code == 404:
            return Response("PointSet introuvable", status=404)
        if resp.status_code != 200:
            return Response("Erreur dépendance externe", status=502)

        # Traitement
        points = bytes_to_point_set(resp.content)
        triangles = triangulate_points(points)
        payload = triangles_to_bytes(points, triangles)

        return Response(payload, mimetype='application/octet-stream')

    except ValueError:
        return Response("Données corrompues reçues du Manager", status=500)
    except requests.exceptions.RequestException:
        return Response("PointSetManager indisponible", status=503)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)