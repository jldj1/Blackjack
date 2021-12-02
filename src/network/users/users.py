from network_config import HOST_URL
import requests

url = HOST_URL

class UserModel:

    @staticmethod
    def create_user(email, username, password):
        try:
            options = {"email": email, "user": username, "password": password}
            response = requests.post(f"{url}/auth/register", data=options)
            return response.json()
        except Exception:
            return {"status": "Server Error"}

    @staticmethod
    def authenticate(username, password):
        try:
            options = {"user": username, "password": password}
            response = requests.post(f"{url}/auth/login", data=options)
            return response.json()
        except Exception:
            return {"status": "Server Error"}

    @staticmethod
    def get_user_info(username):
        try:
            response = requests.get(f"{url}/auth/user/{username}")
            return response.json()
        except Exception:
            return {"status": "Server Error"}

    @staticmethod
    def get_all_users():
        try:
            response = requests.get(f"{url}/auth/users")
            return response.json()
        except Exception:
            return {"status": "Server Error"}

    @staticmethod
    def save_user_info(username, balance):
        try:
            options = {"user": username, "balance": balance}
            response = requests.post(f"{url}/auth/save_balance", data=options)
            return response.json()
        except Exception:
            return {"status": "Server Error"}