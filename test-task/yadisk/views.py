from django.shortcuts import render
import requests
from typing import List, Dict, Any

def get_files_list(public_key: str) -> List[Dict[str, Any]]:

    # Получает список файлов и папок с Яндекс.Диска по публичному ключу.

    url = "https://cloud-api.yandex.net/v1/disk/public/resources?public_key=yMwiideLU18cTEl9nX6xTP4Pr4zd/fcurkJq/S9IJKMVO1XO4WWQqG4f6A48BELVq/J6bpmRyOJonT3VoXnDag=="
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('_embedded', {}).get('items', [])
    return []   

def index(request):

#   Обрабатывает ввод публичного ключа и отображает список файлов и папок.
   
    public_key = request.POST.get('public_key', '')
    files = get_files_list(public_key) if public_key else []
    return render(request, 'yadisk_home.html', {
        'files': files,
        'public_key': public_key
    })