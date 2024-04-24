import json
from app import create_app


def test_create_valid_user():
	payload = {'username': 'valid_username', 'first_name': 'somebody', 'last_name': 'cool', 'email': 'some@email.com'}
	response = create_app().test_client().post('/users', content_type='application/json', json=payload)
	assert response.status_code == 201

	body = json.loads(response.data.decode())
	assert body['username'] == 'valid_username'
	assert body['email'] == 'some@email.com'

test_create_valid_user()
