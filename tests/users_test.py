from . import client

def test_list():
    "Test list all users"
    response = client.get("/users/")
    assert response.status_code == 200

def test_get(id: str):
    "Test get user by id"
    response = client.get("/users/{id}")
    assert response.status_code == 404

def test_create():
    "Test create user"
    response = client.post("/users/", json={})
    assert response.status_code == 201

def test_update(id: str):
    "Test update user by id"
    response = client.put("/users/{id}", json={})

    assert response.status_code == 422

def test_delete(id: str):
    "Test delete user by id"
    response = client.delete("/users/{id}")
    assert response.status_code == 404
