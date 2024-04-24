import json
from app import create_app


def test_list_users():
	response = create_app().test_client().get('/users')
	assert response.status_code == 200

	body = json.loads(response.data.decode())
	assert len(body) == 3


def test_list_users_default_sort():
	response = create_app().test_client().get('/users')
	assert response.status_code == 200

	resp_body = json.loads(response.data.decode())
	assert [user['username'] for user in resp_body] == ['testuser1', 'testuser2', 'validusername']
