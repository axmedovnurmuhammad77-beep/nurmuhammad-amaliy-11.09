import argparse


def start(arguments: argparse.Namespace) -> None:
    print(f"Xizmat ishga tushirildi: {arguments.name}")


def stop(arguments: argparse.Namespace) -> None:
    print(f"Xizmat to'xtatildi: {arguments.name}")


parser = argparse.ArgumentParser(description="Oddiy xizmat boshqaruv CLI'si")
commands = parser.add_subparsers(dest="command", required=True)

start_parser = commands.add_parser("start", help="Xizmatni ishga tushirish")
start_parser.add_argument("--name", default="demo", help="Xizmat nomi")
start_parser.set_defaults(handler=start)

stop_parser = commands.add_parser("stop", help="Xizmatni to'xtatish")
stop_parser.add_argument("--name", default="demo", help="Xizmat nomi")
stop_parser.set_defaults(handler=stop)

arguments = parser.parse_args()
arguments.handler(arguments)