import json
import yaml

with open("api.json", "r", encoding="utf-8") as file:
    json_data = json.load(file)  # Загружаем JSON в Python-словарь

with open("api.yaml", "w", encoding="utf-8") as yaml_file:
    yaml.dump(json_data, yaml_file, allow_unicode=True, default_flow_style=False)

print("Конвертация завершена: api.yaml")
