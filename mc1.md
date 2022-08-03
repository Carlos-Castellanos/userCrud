# Mini Challenge 1

1. Create an 'app' directory.
2. Create an `__init__.py` file within it.
3. Create a file called "routes.py" within app.
4. Create a submodule within app called "database".
5. Create an `__init__.py` file within app/database
6. At the root of your project directory, create a file called setup.sql which should include the following:

```
-- Create the user table
CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(45),
    last_name VARCHAR(45),
    hobbies TEXT,
    active BOOLEAN DEFAULT 1
);
```

Solution:

```
carlos@Charly:~/Code/SDGKU/user_crud$ mkdir app
carlos@Charly:~/Code/SDGKU/user_crud$ mkdir app/database
carlos@Charly:~/Code/SDGKU/user_crud$ touch app/routes.py
carlos@Charly:~/Code/SDGKU/user_crud$ touch app/__init__.py carlos@Charly:~/Code/SDGKU/user_crud$ touch app/database/__init__.py
carlos@Charly:~/Code/SDGKU/user_crud$ touch setup.sql
carlos@Charly:~/Code/SDGKU/user_crud$ ls
```
