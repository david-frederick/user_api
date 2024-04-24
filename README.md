# PYTHON USER API ENDPOINTS

This is a basic Python API allowing for CRUD operations on a User object.

### List All Users
**Request:**

>`GET` http://localhost:5000/users

**Query Parameters:**

These parameters should be added onto the end of the URL using the typical format. Ex:
	`http://localhost:5000/users?order_by=first_name`

- `order_by` allows the user to specify which user attribute should be used for sorting.
  - Available options:
    - `username` (default)
    - `email`
    - `first_name`
    - `last_name`

### Read a User

**Request:**
>`GET` http://localhost:5000/users/username

*Note that "username" within the URL must be replaced with the user's actual username.

### Create a User

**Request:**
>`POST` http://localhost:5000/users

Post requests should have a payload formatted in JSON. See Payload Attributes below for details.

**Payload Attributes:**

- `username`
  - Required.
  - Must be unique.
  - Only alphanumeric characters are accepted.
- `email`
  - Only valid email format is accepted.
- `first_name`
  - Any string accepted.
- `last_name`
  - Any string accepted.

### Update a User
**Request:**
>`PUT` http://localhost:5000/users/username

*Note that "username" within the URL must be replaced with the user's actual username.

Put requests should have a payload formatted in JSON. See Payload Attributes below for details.

**Payload Attributes:**

- `email`
  - Only valid email format is accepted.
- `first_name`
  - Any string accepted.
- `last_name`
  - Any string accepted.

[//]: # (### Delete a User)

[//]: # (**Request:**)
[//]: # (>`DELETE` http://localhost:5000/users/username)

[//]: # ()
[//]: # (*Note that "username" within the URL must be replaced with the user's actual username.)
