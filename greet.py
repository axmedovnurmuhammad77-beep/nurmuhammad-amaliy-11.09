import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Display a greeting.")
    parser.add_argument("--name", required=True, help="Name to greet")
    arguments = parser.parse_args()
    print(f"Salom, {arguments.name}!")


if __name__ == "__main__":
    main()