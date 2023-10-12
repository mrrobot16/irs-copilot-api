import json

def test_health(client):
    response = client.get('/')
    print('test_health(client): response', response)
    # data = json.loads(response.data.decode())
    # assert response.status_code == 200
    # assert data['status'] == 'ok'
