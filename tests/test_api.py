import requests_mock

from src.serializer import point_set_to_bytes


def test_api_nominal(client):
    """Test bout-en-bout avec mock du service externe."""
    points = [(0,0), (10,0), (0,10)]
    fake_binary = point_set_to_bytes(points)
    
    with requests_mock.Mocker() as m:
        # Mock de la réponse du PointSetManager
        m.get("http://point_set_manager:5000/point_sets/123", 
              content=fake_binary, status_code=200)
        
        response = client.get("/triangulation/123")
        
    assert response.status_code == 200
    # Vérifie qu'on a bien reçu du binaire
    assert len(response.data) > len(fake_binary) 

def test_api_manager_404(client):
    with requests_mock.Mocker() as m:
        m.get("http://point_set_manager:5000/point_sets/999", status_code=404)
        response = client.get("/triangulation/999")
    assert response.status_code == 404