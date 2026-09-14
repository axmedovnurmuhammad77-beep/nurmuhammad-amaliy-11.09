class InvalidServerNameError(Exception):
    pass


servers = {
    "web-server": "up",
    "db-server": "down",
    "cache-server": "down",
}


def print_down_servers(monitoring: dict[str, str]) -> None:
    for server, status in monitoring.items():
        if status == "down":
            print(f"Down server: {server}")


def make_greeting(name: str):
    greeting = f"Salom, {name}!"

    def greet() -> str:
        return greeting

    return greet


def check_server_name(name: str) -> None:
    if not name or " " in name or ":" in name:
        raise InvalidServerNameError(f"Noto'g'ri server nomi: {name!r}")
    print(f"Server nomi to'g'ri: {name}")


def validate_port(value: str) -> int:
    try:
        port = int(value)
        if not 1 <= port <= 65535:
            raise ValueError
    except ValueError:
        raise ValueError("Port 1 dan 65535 gacha bo'lgan butun son bo'lishi kerak")
    return port


def main() -> None:
    print("Qaysi topshiriqni bajaramiz?")
    print("0 - Hammasi")
    print("1 - Down serverlar")
    print("2 - List comprehension")
    print("3 - Closure")
    print("4 - Custom exception")
    print("5 - Port validatsiyasi")
    choice = input("Tanlang: ")

    if choice not in {"0", "1", "2", "3", "4", "5"}:
        print("Noto'g'ri tanlov")
        return

    if choice in {"0", "1"}:
        print("\n1. Down serverlar:")
        print_down_servers(servers)

    if choice in {"0", "2"}:
        print("\n2. 1 dan 50 gacha 3 ga bo'linadigan sonlar:")
        print([number for number in range(1, 51) if number % 3 == 0])

    if choice in {"0", "3"}:
        print("\n3. Closure:")
        greeting_function = make_greeting("Ali")
        print(greeting_function())
        print("Ichki funksiya tashqi funksiyadagi name qiymatini eslab qoldi.")

    if choice in {"0", "4"}:
        print("\n4. Custom exception:")
        try:
            check_server_name("web-server")
            check_server_name("bad server")
        except InvalidServerNameError as error:
            print(f"Xatolik: {error}")

    if choice in {"0", "5"}:
        print("\n5. Port validatsiyasi:")
        try:
            port_text = input("Port raqamini kiriting: ")
            print(f"To'g'ri port: {validate_port(port_text)}")
        except ValueError as error:
            print(f"Noto'g'ri format: {error}")


if __name__ == "__main__":
    main()