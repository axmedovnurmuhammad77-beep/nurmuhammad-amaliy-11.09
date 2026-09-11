import csv
import json
import logging
import os
from logging.handlers import RotatingFileHandler

import yaml


def read_config(file_name: str) -> None:
    with open(file_name, encoding="utf-8") as file:
        config = json.load(file)

    logger = logging.getLogger("config")
    logger.handlers.clear()
    logger.setLevel(logging.DEBUG if config.get("debug") is True else logging.INFO)
    logger.addHandler(logging.StreamHandler())
    logger.debug("DEBUG: config = %s", config)
    logger.info("Config o'qildi")


def convert_config(input_name: str, output_name: str) -> None:
    with open(input_name, encoding="utf-8") as file:
        if input_name.lower().endswith((".yaml", ".yml")):
            data = yaml.safe_load(file)
        else:
            data = json.load(file)

    with open(output_name, "w", encoding="utf-8") as file:
        if output_name.lower().endswith((".yaml", ".yml")):
            yaml.safe_dump(data, file, allow_unicode=True, sort_keys=False)
        else:
            json.dump(data, file, ensure_ascii=False, indent=2)
    print(f"Konvertatsiya tayyor: {output_name}")


def filter_error_rows(input_name: str, output_name: str) -> None:
    with open(input_name, newline="", encoding="utf-8") as source:
        reader = csv.DictReader(source)
        with open(output_name, "w", newline="", encoding="utf-8") as target:
            writer = csv.DictWriter(target, fieldnames=reader.fieldnames)
            writer.writeheader()
            count = 0
            for row in reader:
                if row.get("status") == "error":
                    writer.writerow(row)
                    count += 1
    print(f"{count} ta error qator yozildi: {output_name}")


def setup_rotating_logger(file_name: str = "app.log") -> logging.Logger:
    logger = logging.getLogger("rotating")
    logger.handlers.clear()
    logger.setLevel(logging.INFO)
    handler = RotatingFileHandler(
        file_name, maxBytes=1_000_000, backupCount=3, encoding="utf-8"
    )
    logger.addHandler(handler)
    logger.info("Yangi log yozuvi")
    handler.close()
    logger.removeHandler(handler)
    return logger


def create_error_report(folder: str, report_name: str) -> None:
    with open(report_name, "w", encoding="utf-8") as report:
        for name in os.listdir(folder):
            if not name.endswith(".log"):
                continue
            path = os.path.join(folder, name)
            with open(path, encoding="utf-8", errors="replace") as log_file:
                for line_number, line in enumerate(log_file, 1):
                    if "ERROR" in line:
                        report.write(f"{name}:{line_number}: {line}")
    print(f"ERROR hisoboti tayyor: {report_name}")


def main() -> None:
    print("0 - Hammasi")
    print("1 - JSON debug log")
    print("2 - YAML/JSON konverter")
    print("3 - CSV error qatorlari")
    print("4 - 1MB rotating log")
    print("5 - ERROR log hisoboti")
    choice = input("Tanlang: ")

    if choice not in {"0", "1", "2", "3", "4", "5"}:
        print("Noto'g'ri tanlov")
        return
    if choice in {"0", "1"}:
        read_config(input("JSON fayl [config.json]: ") or "config.json")
    if choice in {"0", "2"}:
        convert_config(input("Kirish YAML/JSON fayl: "), input("Chiqish fayl: "))
    if choice in {"0", "3"}:
        filter_error_rows(input("CSV fayl: "), input("Natija CSV: "))
    if choice in {"0", "4"}:
        setup_rotating_logger(input("Log fayli [app.log]: ") or "app.log")
        print("RotatingFileHandler sozlandi: maxBytes=1MB, backupCount=3")
    if choice in {"0", "5"}:
        create_error_report(
            input("Log papka [.]: ") or ".",
            input("Hisobot [error_report.txt]: ") or "error_report.txt",
        )


if __name__ == "__main__":
    main()