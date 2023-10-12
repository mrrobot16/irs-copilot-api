import json

def test_create_user(client):
    print('test_create_user')
    # user_data = {
    #     'name': 'John Doe',
    #     'email': 'john@example.com'
    # }
    # response = client.post('/users', json=user_data)
    # data = json.loads(response.data.decode())

    # assert response.status_code == 201
    # assert data['name'] == user_data['name']
    # assert data['email'] == user_data['email']
    # assert 'id' in data

def test_get_user(client):
    print('test_get_user')
    # # Assuming a user is already present with ID '1'
    # response = client.get('/users/1')
    # data = json.loads(response.data.decode())

    # assert response.status_code == 200
    # assert data['name'] == 'John Doe'
    # assert data['email'] == 'XXXXXXXXXXXXXXXX'
    # assert data['id'] == '1'
    # Assuming a user is already present with ID '1'
    # response = client.get('/users/1')
    # data = json.loads(response.data.decode())

    # assert response.status_code == 200
    # assert data['name'] == 'John Doe'
    # assert data['email'] == 'john@example.com'
    # assert data['id'] == '1'

def test_delete_user(client):
    print('test_delete_user')
    # # Assuming a user is present with ID '1'
    # response = client.delete('/users/1')

    # assert response.status_code == 204

    # # Attempt to retrieve the user again to ensure deletion
    # response = client.get('/users/1')
    # assert response.status_code == 404