from fastapi.testclient import TestClient
from app.api import app

client = TestClient(app)

def test_list_events():
    r = client.get("/events?limit=5")
    assert r.status_code == 200
    assert isinstance(r.json(), list)

def test_get_event_not_found():
    r = client.get("/events/999999")
    assert r.status_code == 404
