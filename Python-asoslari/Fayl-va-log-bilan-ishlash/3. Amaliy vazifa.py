import csv
import json
import logging
import yaml


logging.basicConfig(
    filename="important_events.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)


print("1. Log yozuvlari:")
with open("activity.log", "a", encoding="utf-8") as log_file:
    for number in range(1, 6):
        log_file.write(f"Log yozuvi {number}\n")
print("5 ta log yozuvi activity.log fayliga qo'shildi")


print("\n2. JSON konfiguratsiya:")
config = {"env": "development", "port": 8080, "debug": True}
with open("config.json", "w", encoding="utf-8") as config_file:
    json.dump(config, config_file, indent=2)
with open("config.json", encoding="utf-8") as config_file:
    print(json.load(config_file))


print("\n3. YAML serverlar:")
servers = {"servers": [{"name": "web", "ip": "192.168.1.10"}, {"name": "db", "ip": "192.168.1.20"}]}
with open("servers.yaml", "w", encoding="utf-8") as yaml_file:
    yaml.safe_dump(servers, yaml_file, sort_keys=False)
with open("servers.yaml", encoding="utf-8") as yaml_file:
    print(yaml.safe_load(yaml_file))


print("\n4. Xodimlar jadvali:")
employees = [
    ["id", "name", "department"],
    [1, "Ali", "DevOps"],
    [2, "Vali", "Python"],
    [3, "Salim", "QA"],
]
with open("employees.csv", "w", newline="", encoding="utf-8") as csv_file:
    csv.writer(csv_file).writerows(employees)
with open("employees.csv", newline="", encoding="utf-8") as csv_file:
    for row in csv.reader(csv_file):
        print(" | ".join(row))


logging.info("Skript muvaffaqiyatli tugadi")
print("\n5. Muhim voqealar important_events.log fayliga yozildi")
