import json
import yaml
import requests
import os
import subprocess

# URL FastAPI сервиса (замени при необходимости)
API_URL = "http://127.0.0.1:8000/openapi.json"

# Путь к файлам
JSON_FILE = "api.json"
YAML_FILE = "api.yaml"

# Репозиторий API-контракта
GIT_REPO_URL = "git@github.com:5Evo/aiw-api-contract.git"
GIT_DIR = "api-contract"


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


def update_git_repo():
    """Клонирует репозиторий, обновляет файлы и отправляет изменения"""
    if not os.path.exists(GIT_DIR):
        subprocess.run(["git", "clone", GIT_REPO_URL, GIT_DIR], check=True)

    os.chdir(GIT_DIR)
    subprocess.run(["git", "pull"], check=True)

    os.replace(f"../{JSON_FILE}", JSON_FILE)
    os.replace(f"../{YAML_FILE}", YAML_FILE)

    subprocess.run(["git", "add", JSON_FILE, YAML_FILE], check=True)
    subprocess.run(["git", "commit", "-m", "Автообновление OpenAPI контракта"], check=True)
    subprocess.run(["git", "push"], check=True)

    print("✅ API-контракт обновлён в репозитории")
    os.chdir("..")


if __name__ == "__main__":
    download_openapi()
    convert_to_yaml()
    update_git_repo()
