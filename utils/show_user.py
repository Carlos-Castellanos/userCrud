import requests

URL= "http://127.0.0.1:5000/users/"

def show_user(fid):
    completeURL=URL+fid
    response = requests.get(completeURL)
    if response.status_code == 200:
        print(
            "succesfully found record; Got:    %s"
            % response.json().get("users")      
        )
    else:
        print(
            "something went wrong while tryin go show an user. "
        )

if __name__ == "__main__":
    fid = input("Type in the user'id: ")

    show_user(fid)
