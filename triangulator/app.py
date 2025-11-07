"""API Flask du service Triangulator."""

import struct
import io
import requests
from flask import Flask, request, send_file, jsonify
from .binary_format import decode_pointset, encode_pointset
from .triangulation import triangulate

app = Flask(__name__)


@app.route('/triangulate', methods=['POST'])
def triangulate_endpoint():
    """Endpoint principal pour demander une triangulation.

    Attend un JSON avec 'pointSetId'.
    Récupère les points via PointSetManager, calcule la triangulation,
    et renvoie le résultat en binaire.

    Returns:
        Response: Données binaires de type Triangles ou erreur JSON.
    """
    pointset_id = request.json.get('pointSetId')
    if not pointset_id:
        return jsonify({"error": "pointSetId requis"}), 400

    try:
        resp = requests.get(f"http://localhost:5001/pointsets/{pointset_id}")
        if resp.status_code == 404:
            return jsonify({"error": "PointSet non trouvé"}), 404
        if resp.status_code != 200:
            return jsonify({"error": "PointSetManager erreur"}), 500

        points = decode_pointset(resp.content)
        triangles = triangulate(points)

        # Encoder les sommets (format PointSet)
        out_data = encode_pointset(points)
        # Encoder le nombre de triangles
        out_data += struct.pack("I", len(triangles))
        # Encoder chaque triangle (3 indices unsigned long)
        for a, b, c in triangles:
            out_data += struct.pack("III", a, b, c)

        return send_file(io.BytesIO(out_data), mimetype='application/octet-stream')

    except Exception as e:
        return jsonify({"error": str(e)}), 500
