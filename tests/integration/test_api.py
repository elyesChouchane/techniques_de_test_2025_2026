"""Tests d'intégration de l'API HTTP."""
import pytest
from unittest.mock import patch
from triangulator.app import app


@pytest.fixture
def client():
    """Fournit un client de test Flask."""
    app.config['TESTING'] = True
    return app.test_client()


@patch('triangulator.app.requests.get')
def test_api_success(mock_get, client):
    """Test du cas nominal : triangulation réussie."""
    binary_data = (
        b'\x03\x00\x00\x00'
        b'\x00\x00\x00\x00\x00\x00\x00\x00'
        b'\x00\x00\x80?\x00\x00\x00\x00'
        b'\x00\x00\x00@\x00\x00\x80?'
    )
    mock_get.return_value.status_code = 200
    mock_get.return_value.content = binary_data
    response = client.post('/triangulate', json={'pointSetId': '123'})
    assert response.status_code == 200
    assert response.content_type == 'application/octet-stream'


@patch('triangulator.app.requests.get')
def test_api_not_found(mock_get, client):
    """Test avec PointSetID inexistant → 404."""
    mock_get.return_value.status_code = 404
    response = client.post('/triangulate', json={'pointSetId': '999'})
    assert response.status_code == 404
