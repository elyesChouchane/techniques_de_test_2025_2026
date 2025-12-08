"""
Module responsable de la sérialisation et désérialisation binaire.
Respecte le protocole défini: Count (4B) + Points (8B each).
"""
import struct


def point_set_to_bytes(points: list[tuple[float, float]]) -> bytes:
    """Convertit une liste de points en format binaire."""
    buffer = bytearray()
    # 'I' = unsigned int (4 bytes) pour le nombre de points
    buffer.extend(struct.pack('<I', len(points)))
    for x, y in points:
        # 'ff' = deux floats (4 bytes chacun)
        buffer.extend(struct.pack('<ff', float(x), float(y)))
    return bytes(buffer)


def bytes_to_point_set(data: bytes) -> list[tuple[float, float]]:
    """Lit le format binaire pour récupérer les points."""
    if len(data) < 4:
        raise ValueError("Données trop courtes pour contenir un header.")

    count = struct.unpack('<I', data[:4])[0]
    expected_size = 4 + count * 8

    if len(data) < expected_size:
        raise ValueError(
            f"Taille incorrecte. Attendu: {expected_size}, Reçu: {len(data)}"
        )

    points = []
    offset = 4
    for _ in range(count):
        x, y = struct.unpack('<ff', data[offset : offset + 8])
        points.append((x, y))
        offset += 8
    return points


def triangles_to_bytes(
    points: list[tuple[float, float]], triangles: list[tuple[int, int, int]]
) -> bytes:
    """
    Construit la réponse binaire finale.
    Format: [PointSet Binaire] + [Count Triangles (4B)] + [Indices (12B each)]
    """
    # 1. On réutilise le binaire des points
    buffer = bytearray(point_set_to_bytes(points))

    # 2. Nombre de triangles
    buffer.extend(struct.pack('<I', len(triangles)))

    # 3. Les triangles (3 indices d'entiers non signés)
    for t1, t2, t3 in triangles:
        buffer.extend(struct.pack('<III', t1, t2, t3))

    return bytes(buffer)