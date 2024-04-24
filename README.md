# PYTHON USER API ENDPOINTS

This is a basic Python API allowing for CRUD operations on a User object.

### List All Users
**Request:**

`GET` http://localhost:5000/users

**Query Parameters:**

- `order_by` allows the user to specify which user attribute should be used for sorting.
  - Default value: "username"

### Read a User

**Request:**

`GET` http://localhost:5000/users/username

*Note that "username" within the URL must be replaced with the user's actual username.

### Create a User

`POST` http://localhost:5000/users

### Update a User
`PUT` http://localhost:5000/users/username

*Note that "username" within the URL must be replaced with the user's actual username.

[//]: # (### Delete a User)

[//]: # (`DELETE` http://localhost:5000/users/username)

[//]: # ()
[//]: # (*Note that "username" within the URL must be replaced with the user's actual username.)
