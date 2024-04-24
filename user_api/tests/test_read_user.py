import json
from app import create_app


def test_valid_username():
	response = create_app().test_client().get('/users/test_user1')
	assert response.status_code == 200
	body = json.loads(response.data.decode())
	assert body == {
		'username': 'test_user1',
		'email': 'test@testing.com',
		'first_name': 'Test',
		'last_name': 'Testerson'
	}


def test_bad_username():
	response = create_app().test_client().get('/users/bad_username')
	assert response.status_code == 404
