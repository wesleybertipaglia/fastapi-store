from . import client

def test_list():
    "Test list all products"
    response = client.get("/products/")
    assert response.status_code == 200

def test_get(id: str):
    "Test get product by id"
    response = client.get("/products/{id}")
    assert response.status_code == 404

def test_create():
    "Test create product"
    response = client.post("/products/", json={})
    assert response.status_code == 201

def test_update(id: str):
    "Test update product by id"
    response = client.put("/products/{id}", json={})

    assert response.status_code == 422

def test_delete(id: str):
    "Test delete product by id"
    response = client.delete("/products/{id}")
    assert response.status_code == 404
