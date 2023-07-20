from conftest import client


def test_upload_file(prepare_database, access_token):
    with open(f'./tests/csv-examples/dummy.csv', 'rb') as binary_file: 
        response = client.post(
            '/files', headers={
            'Authorization': f'Bearer {access_token}'},
            files={'file': ('dummy.csv', binary_file, 'text/csv')})
        assert response.status_code == 201


def test_download_file(prepare_database, access_token):
    response = client.get('/files/dummy.csv', headers={
        'Authorization': f'Bearer {access_token}'
    })
    assert response.status_code == 200


def test_get_all_metadata(prepare_database, access_token):
    response = client.get('/metadata', headers={
        'Authorization': f'Bearer {access_token}'
    })
    assert response.status_code == 200


def test_get_metadata(prepare_database, access_token):
    response = client.get('/metadata/dummy.csv', headers={
        'Authorization': f'Bearer {access_token}'
    })
    assert response.status_code == 200
    

def test_remove_file(prepare_database, access_token):
    response = client.delete('/files/dummy.csv', headers={
        'Authorization': f'Bearer {access_token}'
    })
    assert response.status_code == 204