import argparse
from pathlib import Path


def count_files(folder: Path) -> int:
    return sum(path.is_file() for path in folder.iterdir())


def main() -> None:
    parser = argparse.ArgumentParser(description="Count files in a folder.")
    parser.add_argument("folder", nargs="?", default=".", help="Folder to inspect")
    arguments = parser.parse_args()
    folder = Path(arguments.folder)

    if not folder.is_dir():
        parser.error(f"Folder does not exist: {folder}")
    print(count_files(folder))


if __name__ == "__main__":
    main()