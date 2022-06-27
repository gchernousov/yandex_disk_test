import requests
from pprint import pprint as pp


MAIN_URL = 'https://cloud-api.yandex.net'


def get_token():
    with open("token.txt") as token_file:
        token = token_file.read()
        return token


def create_folder(folder_name):
    token = get_token()
    url = MAIN_URL + '/v1/disk/resources'
    params = {'path': folder_name}
    headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {token}'}
    res = requests.put(url, params=params, headers=headers)
    return res.status_code


def get_folder_info(folder_name):
    token = get_token()
    url = MAIN_URL + '/v1/disk/resources'
    params = {'path': folder_name}
    headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {token}'}
    res = requests.get(url, params=params, headers=headers)
    return res


if __name__ == "__main__":

    folder_name = input("Enter folder name to create: ")

    create_folder(folder_name)
    folder_info = get_folder_info(folder_name).json

    pp(folder_info)