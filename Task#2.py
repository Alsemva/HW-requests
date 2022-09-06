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
        response.raise_for_status()
        return response.json()

    def upload(self, path_to_dir, file_list):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        for file_path in file_list:
            response_dict = self._get_upload_url(f'{path_to_dir}/{file_path}')
            upload_files_url = response_dict.get("href", "")
            with open(f'{path_to_dir}/{file_path}', 'rb') as file:
                response = requests.put(upload_files_url, files={"file": file})
                response.raise_for_status()
                if response.status_code == 201:
                    print('Status: OK')
        return 'Done'


def token_from_file():
    with open('token.txt') as t_file:
        token_f = t_file.read()
    return token_f


if __name__ == '__main__':
    path_to_dir = 'files'
    path_to_file = listdir(path_to_dir)
    token = token_from_file()
    uploader = YaUploader(token)
    result = uploader.upload(path_to_dir, path_to_file)
    print(result)
