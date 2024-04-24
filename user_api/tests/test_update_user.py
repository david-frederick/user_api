import json
from app import create_app


def test_update_valid_attribute():
	payload = {'first_name': 'somebody', 'last_name': 'cool'}
	response = create_app().test_client().put('/users/test_user1', content_type='application/json', json=payload)
	assert response.status_code == 200

	body = json.loads(response.data.decode())
	assert body['username'] == 'test_user1'
	assert body['first_name'] == 'somebody'


def test_update_username_rejected():
	payload = {'username': 'test_user3'}
	response = create_app().test_client().put('/users/test_user1', content_type='application/json', json=payload)
	assert response.status_code == 422


def test_update_invalid_user():
	payload = {'first_name': 'whatever'}
	response = create_app().test_client().put('/users/bad_username', content_type='application/json', json=payload)
	assert response.status_code == 404
