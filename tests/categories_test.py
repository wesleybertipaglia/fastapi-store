from . import client

def test_list():
    "Test list all categories"
    response = client.get("/categories/")
    assert response.status_code == 200

def test_get(id: str):
    "Test get category by id"
    response = client.get("/categories/{id}")
    assert response.status_code == 404

def test_create():
    "Test create category"
    response = client.post("/categories/", json={})
    assert response.status_code == 201

def test_update(id: str):
    "Test update category by id"
    response = client.put("/categories/{id}", json={})

    assert response.status_code == 422

def test_delete(id: str):
    "Test delete category by id"
    response = client.delete("/categories/{id}")
    assert response.status_code == 404
