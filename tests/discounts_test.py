from . import client

def test_list():
    "Test list all discounts"
    response = client.get("/discounts/")
    assert response.status_code == 200

def test_get(id: str):
    "Test get discount by id"
    response = client.get("/discounts/{id}")
    assert response.status_code == 404

def test_create():
    "Test create discount"
    response = client.post("/discounts/", json={})
    assert response.status_code == 201

def test_update(id: str):
    "Test update discount by id"
    response = client.put("/discounts/{id}", json={})

    assert response.status_code == 422

def test_delete(id: str):
    "Test delete discount by id"
    response = client.delete("/discounts/{id}")
    assert response.status_code == 404
