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


def test_list_users_custom_order():
	response = create_app().test_client().get('/users?order_by=first_name')
	assert response.status_code == 200

	resp_body = json.loads(response.data.decode())
	assert [user['first_name'] for user in resp_body] == ['CFA', 'somebody', 'Test']


def test_list_users_invalid_sort():
	response = create_app().test_client().get('/users?order_by=invalid_column')
	assert response.status_code == 404
