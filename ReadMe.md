# AIW API Contracts

Этот проект предназначен для автоматического получения OpenAPI-контракта FastAPI-сервиса и его сохранения в JSON и YAML форматах.

## Структура проекта

```
AIW-API-CONTRACTS/
├── api.json                # Файл с OpenAPI-контрактом в формате JSON
├── api.yaml                # Файл с OpenAPI-контрактом в формате YAML
├── update_api_contract.py  # Скрипт для получения OpenAPI-контракта
├── .gitignore              # Файл с исключениями для Git
├── README.md               # Документация проекта
└── requirements.txt        # Список зависимостей
```

## Требования

- Python 3.8+
- FastAPI-сервис, доступный по API
- Установленные зависимости (указаны в `requirements.txt`)

## Установка

1. Клонировать репозиторий:
   ```bash
   git clone git@github.com:5Evo/aiw-api-contract.git
   cd aiw-api-contract
   ```

2. Создать и активировать виртуальное окружение:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Для Linux/macOS
   .venv\Scripts\activate     # Для Windows
   ```

3. Установить зависимости:
   ```bash
   pip install -r requirements.txt
   ```

## Использование

1. Убедиться, что FastAPI-сервис запущен и доступен по адресу `http://127.0.0.1:8000/openapi.json`.
2. Запустить скрипт для обновления OpenAPI-контрактов:
   ```bash
   python update_api_contract.py
   ```
3. После успешного выполнения появятся или обновятся файлы `api.json` и `api.yaml`.
4. Закоммитить и запушить изменения вручную, если требуется:
   ```bash
   git add api.json api.yaml
   git commit -m "Обновлен OpenAPI контракт"
   git push origin master
   ```

## Детали работы `update_api_contract.py`

Скрипт выполняет следующие шаги:

1. Получает OpenAPI-контракт в формате JSON по указанному API-адресу.
2. Сохраняет полученные данные в `api.json`.
3. Преобразует JSON в YAML и сохраняет в `api.yaml`.

## Возможные ошибки и их решение

### 1. Ошибка подключения к API (`Ошибка загрузки OpenAPI`)
**Решение:**
- Проверь, запущен ли FastAPI-сервис.
- Убедись, что API доступен по `http://127.0.0.1:8000/openapi.json`.

### 2. Ошибка `Permission denied (publickey)` при клонировании репозитория
**Решение:**
- Добавь свой SSH-ключ в GitHub: `ssh-add ~/.ssh/id_rsa`.
- Проверь настройки SSH-доступа с помощью `ssh -T git@github.com`.

## Авторы

- **[Твое имя]** – Разработчик проекта

## Лицензия

Copyright (c) [2025] [aiWorkers]. All rights reserved.
