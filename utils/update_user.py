import requests

URL= "http://127.0.0.1:5000/users/"

def update_user(first_name,last_name,hobbies,id):
    user = {
        "first_name":first_name,
        "last_name":last_name,
        "hobbies":hobbies
    }
    URL_id=URL+id
    print(URL_id)
    response = requests.put(URL_id, json=user)
    if response.status_code == 204:
        print(
            "succesfully update record; Got:"
           
        )
    else:
        print(
            "something went wrong while tryin go modify a new user. "
        )

if __name__ == "__main__":
    fname = input("Type in the user'first name: ")
    lname = input("Type in the user'last name: ")
    hobbies = input("Type in the user'hobbies: ")
    id      = input("Type in the user'id: ")
    update_user(fname,lname,hobbies,id)
