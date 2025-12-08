import struct

import pytest

from src.serializer import bytes_to_point_set, point_set_to_bytes


def test_point_set_serialization_nominal():
    points = [(1.0, 2.0), (3.5, 4.5)]
    data = point_set_to_bytes(points)
    
    # 4 bytes (count) + 2 * 8 bytes (points) = 20 bytes
    assert len(data) == 20
    assert struct.unpack('<I', data[:4])[0] == 2

def test_bytes_to_point_set_nominal():
    # Construction manuelle d'un binaire valide (1 point: 10.0, 20.0)
    data = struct.pack('<Iff', 1, 10.0, 20.0)
    points = bytes_to_point_set(data)
    
    assert len(points) == 1
    assert points[0] == (10.0, 20.0)

def test_bytes_to_point_set_invalid_size():
    data = b'\x01\x00\x00\x00' # Dit qu'il y a 1 point, mais s'arrête là
    with pytest.raises(ValueError):
        bytes_to_point_set(data)