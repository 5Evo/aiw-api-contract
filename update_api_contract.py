import json
import yaml
import requests
import os

# URL FastAPI сервиса (замени при необходимости)
API_URL = "http://127.0.0.1:8000/openapi.json"

# Пути к файлам
JSON_FILE = "api.json"
YAML_FILE = "api.yaml"

def download_openapi():
    """Скачивает OpenAPI JSON из запущенного сервиса"""
    response = requests.get(API_URL)
    if response.status_code == 200:
        with open(JSON_FILE, "w", encoding="utf-8") as file:
            file.write(response.text)
        print(f"✅ OpenAPI JSON сохранён в {JSON_FILE}")
    else:
        print(f"❌ Ошибка загрузки OpenAPI: {response.status_code}")
        exit(1)

def convert_to_yaml():
    """Конвертирует JSON в YAML"""
    with open(JSON_FILE, "r", encoding="utf-8") as file:
        json_data = json.load(file)

    with open(YAML_FILE, "w", encoding="utf-8") as yaml_file:
        yaml.dump(json_data, yaml_file, allow_unicode=True, default_flow_style=False)

    print(f"✅ OpenAPI YAML сохранён в {YAML_FILE}")

if __name__ == "__main__":
    download_openapi()
    convert_to_yaml()
    print("✅ Обновление OpenAPI контракта завершено. Не забудьте закоммитить изменения вручную!")
