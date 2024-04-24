import json
from app import create_app


def test_list_users():
	response = create_app().test_client().get('/users')
	assert response.status_code == 200

	body = json.loads(response.data.decode())
	assert len(body) == 3


def test_list_users_default_order_by():
	response = create_app().test_client().get('/users')
	assert response.status_code == 200

	resp_body = json.loads(response.data.decode())
	assert [user['username'] for user in resp_body] == ['testuser1', 'testuser2', 'validusername']


def test_list_users_custom_order_by():
	response = create_app().test_client().get('/users?order_by=first_name')
	assert response.status_code == 200

	resp_body = json.loads(response.data.decode())
	assert [user['first_name'] for user in resp_body] == ['CFA', 'somebody', 'Test']


def test_list_users_invalid_order_by():
	response = create_app().test_client().get('/users?order_by=invalid_column')
	assert response.status_code == 404


def test_list_users_reverse_order():
	response = create_app().test_client().get('/users?order=desc')
	assert response.status_code == 200

	body = json.loads(response.data.decode())
	assert len(body) == 3
	assert body[0]['username'] == 'validusername'
