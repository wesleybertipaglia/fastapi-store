from . import client

def test_list():
    "Test list all payments_methods"
    response = client.get("/payments_methods/")
    assert response.status_code == 200

def test_get(id: str):
    "Test get payment_method by id"
    response = client.get("/payments_methods/{id}")
    assert response.status_code == 404

def test_create():
    "Test create payment_method"
    response = client.post("/payments_methods/", json={})
    assert response.status_code == 201

def test_update(id: str):
    "Test update payment_method by id"
    response = client.put("/payments_methods/{id}", json={})

    assert response.status_code == 422

def test_delete(id: str):
    "Test delete payment_method by id"
    response = client.delete("/payments_methods/{id}")
    assert response.status_code == 404
