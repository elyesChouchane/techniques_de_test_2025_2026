import struct

def encode_pointset(points):
    data = struct.pack("I", len(points))
    for x, y in points:
        data += struct.pack("ff", x, y)
    return data

def decode_pointset(data):
    if len(data) < 4:
        raise ValueError("Données trop courtes")
    n = struct.unpack("I", data[:4])[0]
    expected_len = 4 + 8 * n
    if len(data) != expected_len:
        raise ValueError(f"Taille incorrecte: attendu {expected_len}, reçu {len(data)}")
    points = []
    for i in range(n):
        offset = 4 + 8 * i
        x, y = struct.unpack("ff", data[offset:offset+8])
        points.append((x, y))
    return points