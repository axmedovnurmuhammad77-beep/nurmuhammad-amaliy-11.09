def even_numbers(numbers: list[int]) -> list[int]:
    return [number for number in numbers if number % 2 == 0]


servers = {
    "web-server": "192.168.1.10",
    "db-server": "192.168.1.20",
    "cache-server": "192.168.1.30",
}


def divide(first_number: float, second_number: float) -> None:
    try:
        print(f"Natija: {first_number / second_number}")
    except ZeroDivisionError:
        print("Xatolik: ikkinchi sonni nolga bo'lish mumkin emas")


print("1. Juft sonlar:")
print(even_numbers([1, 2, 3, 4, 5, 6, 7, 8]))

print("\n2. Serverlar va IP manzillar:")
for server, ip_address in servers.items():
    print(f"{server}: {ip_address}")

print("\n3. 1 dan 100 gacha yig'indi:")
total = 0
for number in range(1, 101):
    total += number
print(total)

print("\n4. Butun son tekshiruvi:")
try:
    number_text = input("Butun son kiriting: ")
    number = int(number_text)
    print(f"Siz kiritgan son: {number}")
except ValueError:
    print("Xatolik: butun son kiritishingiz kerak")

print("\n5. Bo'lish:")
try:
    first = float(input("Birinchi sonni kiriting: "))
    second = float(input("Ikkinchi sonni kiriting: "))
    divide(first, second)
except ValueError:
    print("Xatolik: faqat son kiriting")
