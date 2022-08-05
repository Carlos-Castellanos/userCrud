import requests

URL= "http://127.0.0.1:5000/users/"

def delete_user(fid):
    completeURL=URL+fid
    response = requests.delete(completeURL)
    if response.status_code == 204:
        print(
            "succesfully deleted record; Got:"  
        )
    else:
        print(
            "something went wrong while tryin go delete an user. "
        )

if __name__ == "__main__":
    fid = input("Type in the user'id: ")

    delete_user(fid)
