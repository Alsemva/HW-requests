import requests
from os import listdir

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Authorization': f'OAuth {self.token}'
        }

    def _get_upload_url(self, file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload(self, path_to_dir):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        # for file_path in file_list:
        response_dict = self._get_upload_url(path_to_dir)
        upload_files_url = response_dict.get("href", "")
        with open(path_to_dir, 'rb') as file:
            response = requests.put(upload_files_url, files={"file": file})
        print(response)
        # Функция может ничего не возвращать

def token():
    with open('token.txt', encoding='utf-8') as t_file:
        token_f = t_file.read()
    return token_f


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    # path_to_dir = 'files'
    # path_to_file = listdir(path_to_dir)
    path_to_file = 'files/list.txt'
    token = token()
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
