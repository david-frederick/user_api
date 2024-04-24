import json
from app import create_app


def test_list_users():
	response = create_app().test_client().get('/users')
	assert response.status_code == 200

	body = json.loads(response.data.decode())
	assert len(body) == 3
	assert body[0]['username'] == 'test_user1'
	assert body[1]['username'] == 'test_user2'
