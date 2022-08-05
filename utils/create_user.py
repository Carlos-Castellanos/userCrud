import requests

URL= "http://127.0.0.1:5000/users"

def create_user(first_name,last_name,hobbies):
    user = {
        "first_name":first_name,
        "last_name":last_name,
        "hobbies":hobbies
    }
    response = requests.post(URL, json=user)
    if response.status_code == 201:
        print(
            "succesfully created new record; Got: %s"
            % response.json().get("message")
        )
    else:
        print(
            "something went wrong while tryin go create a new user. "
        )

if __name__ == "__main__":
    fname = input("Type in the user' first name: ")
    lname = input("Type in the user' last name: ")
    hobbies = input("Type in the user' hobbies: ")
    create_user(fname,lname,hobbies)
