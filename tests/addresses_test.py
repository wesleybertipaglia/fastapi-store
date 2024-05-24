from . import client

def test_list():
    "Test list all addresses"
    response = client.get("/address/")
    assert response.status_code == 200

def test_get(id: str):
    "Test get address by id"
    response = client.get("/address/{id}")
    assert response.status_code == 404

def test_create():
    "Test create address"
    response = client.post("/address/", json={})
    assert response.status_code == 201

def test_update(id: str):
    "Test update address by id"
    response = client.put("/address/{id}", json={})

    assert response.status_code == 422

def test_delete(id: str):
    "Test delete address by id"
    response = client.delete("/address/{id}")
    assert response.status_code == 404
