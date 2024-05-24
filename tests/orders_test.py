from . import client

def test_list():
    "Test list all orders"
    response = client.get("/orders/")
    assert response.status_code == 200

def test_get(id: str):
    "Test get order by id"
    response = client.get("/orders/{id}")
    assert response.status_code == 404

def test_create():
    "Test create order"
    response = client.post("/orders/", json={})
    assert response.status_code == 201

def test_update(id: str):
    "Test update order by id"
    response = client.put("/orders/{id}", json={})

    assert response.status_code == 422

def test_delete(id: str):
    "Test delete order by id"
    response = client.delete("/orders/{id}")
    assert response.status_code == 404
