# In place of true persistance, I'm just using a basic object to store
# users in memory. I've pulled this into its own file to help minimize
# the number of code changes needed if a database was to be added.
users = {
	'test_user1': {
		'username': 'test_user1',
		'first_name': 'Test',
		'last_name': 'Testerson',
		'email': 'test@testing.com'
	},
	'test_user2': {
		'username': 'test_user2',
		'first_name': 'CFA',
		'last_name': 'Guy',
		'email': 'cfa_guy@something.com'
	},
}
