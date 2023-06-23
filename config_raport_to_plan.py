from yaml import safe_load


# читаем конфиг
try:
    with open("config_raport_to_plan.yml", 'r', encoding='utf-8') as f:
        config = safe_load(f)
except:
    print("Файл конфигуратора .yml не найден")
    exit()  # завершаем программу
# если файл пустой завершаю выполнение скрипта

try:
    len(config)
except:
    print("Файл конфигуратора .yml пустой. Необходимо заполнить файл, затем запустить программу заново.")
    exit()  # завершаем программу

print(f"Применены следующие исходные параметры для формирования файла: {config}")
