import requests
from pprint import pprint

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path):
        """Метод загружает файл file_path на Яндекс.Диск"""
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}
        params = {"path": f"Нетология/{filename}", "overwrite": "true"}
        response_1 = requests.get(upload_url, headers=headers, params=params).json()
        pprint(response_1)
        href = response_1.get("href", "")
        responce_2 = requests.put(href, data=open(file_path, 'rb'))
        pprint(f"Operation status_code: {responce_2.status_code}")
        responce_2.raise_for_status()
        if responce_2.status_code == 201:
            return 'Success'
        else:
            return f"Ошибка! Код ошибки: {responce_2.status_code}"


if __name__ == '__main__':
    path_to_file = '' # сюда вписываем путь до файла 
    filename = path_to_file.split('/')[-1] 
    token = ''  # здесь указываем свой token
    uploader = YaUploader(token)
    print(f"Идет загрузка файла {filename}")
    result = uploader.upload(path_to_file)
    print(result)
    
    
    
