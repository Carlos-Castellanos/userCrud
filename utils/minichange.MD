# Mini challenge 2

### Create scripts to manually test our update and our deactivate endpoints.

To issue a PUT request, you can use the "put()" function associated with the requests module like so:
```
response = requests.put(URL, json=SOMETHING)
```

To issue a DELETE request, you can use the "delete()" function associated with the requests module, like so:

```
response = requests.delete(URL)
```

## Instructions:

1. Create a file under utils called "update_user.py"
    1.1. This file should request an ID, a first_name a last_name and hobbies.
    1.2. The file should contain a function that issues a PUT request to the appropriate URL for our API.
2. Create a file under utils called "deactivate_user.py"
    1.1. This file should request an ID.
    1.2. The file should contain a function that issues a DELETE request to the appropriate URL for our API.
