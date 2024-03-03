from fastapi.testclient import TestClient

from bigbardawannabe2.app import app


def test_root():
    """Check if root endpoint returns correct message."""
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == 200
    assert response.json() == {'message': 'Welcome to BigBardaWannabe!'}
