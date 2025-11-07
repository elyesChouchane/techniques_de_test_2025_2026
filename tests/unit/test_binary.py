from triangulator.binary_format import encode_pointset, decode_pointset

def test_encode_decode():
    pts = [(1.0, 2.0), (3.0, 4.0)]
    data = encode_pointset(pts)
    assert decode_pointset(data) == pts

def test_empty_pointset():
    data = encode_pointset([])
    assert decode_pointset(data) == []