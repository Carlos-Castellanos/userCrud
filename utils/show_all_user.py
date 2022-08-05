import requests

URL= "http://127.0.0.1:5000/users"

def show_all_user():
    
    response = requests.get(URL)
    if response.status_code == 200:
        all_user=response.json().get("users");
        print(
            "User List"
        )

        for user in all_user:
            print("User Name:  "
                +user["first_name"]+" "+user["last_name"]+
                "  Hobbies:"+
                user["hobbies"]
                )

    else:
        print(
            "something went wrong while tryin go show an user. "
        )

if __name__ == "__main__":
    show_all_user()
