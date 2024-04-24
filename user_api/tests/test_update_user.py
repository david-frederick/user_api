import json
from app import create_app


def test_update_valid_user():
	payload = {'first_name': 'somebody', 'last_name': 'cool', 'email': 'some@email.com'}
	response = create_app().test_client().put('/users/test_user1', content_type='application/json', json=payload)
	assert response.status_code == 200

	body = json.loads(response.data.decode())
	assert body['username'] == 'test_user1'
	assert body['first_name'] == 'somebody'
