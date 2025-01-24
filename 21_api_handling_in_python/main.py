import requests


def fetch_random_user_data():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()

    if "data" in data and data["success"] == True:
        user_data = data["data"]
        username = user_data["login"]["username"]
        country = user_data["location"]["coordinates"]
        return (username, country)
    else:
        raise Exception("Failed to fetch user data.")


def main():
    try:
        res = fetch_random_user_data()
        print(f"username: {res[0]}, country: {res[1]}")
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()
