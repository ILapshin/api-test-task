import pytest

from conftest import client


@pytest.mark.first
def test_create_user(fake_user, prepare_database):
    response = client.post('/users', json=fake_user)
    assert response.status_code == 201

def test_get_user(fake_user, prepare_database):
    response = client.get('/users/2')
    assert response.status_code == 200
    assert response.json()['name'] == fake_user['name']    
    assert response.json()['email'] == fake_user['email']