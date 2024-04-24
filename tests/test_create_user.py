import json
from app import create_app


def test_create_valid_user():
	payload = {'username': 'validusername', 'first_name': 'somebody', 'last_name': 'cool', 'email': 'some@email.com'}
	response = create_app().test_client().post('/users', content_type='application/json', json=payload)
	assert response.status_code == 201

	body = json.loads(response.data.decode())
	assert body['username'] == 'validusername'
	assert body['email'] == 'some@email.com'


def test_reject_non_unique_username():
	payload = {'username': 'testuser1', 'first_name': 'somebody', 'last_name': 'cool', 'email': 'some@email.com'}
	response = create_app().test_client().post('/users', content_type='application/json', json=payload)
	assert response.status_code == 409


def test_reject_invalid_username():
	payload = {'username': 'bad_username&1234', 'first_name': 'somebody', 'last_name': 'cool', 'email': 'some@email.com'}
	response = create_app().test_client().post('/users', content_type='application/json', json=payload)
	assert response.status_code == 422


def test_reject_invalid_email():
	payload = {'username': 'valid', 'first_name': 'somebody', 'last_name': 'cool', 'email': 'bad'}
	response = create_app().test_client().post('/users', content_type='application/json', json=payload)
	assert response.status_code == 422
