# In place of true persistance, I'm just using a basic object to store
# users in memory. I've pulled this into its own file to help minimize
# the number of code changes needed if a database was to be added.
users = {
	'testuser1': {
		'username': 'testuser1',
		'first_name': 'Test',
		'last_name': 'Testerson',
		'email': 'test@testing.com'
	},
	'testuser2': {
		'username': 'testuser2',
		'first_name': 'CFA',
		'last_name': 'Guy',
		'email': 'cfa_guy@something.com'
	},
}
