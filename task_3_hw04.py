# Пороблено Chat CPT ;-)

from pathlib import Path
from colorama import init, Fore, Style
import sys

init(autoreset=True)

def print_dir_structure(start_path, indent="", is_root=True):
    start_path = Path(start_path)
    if is_root:
        print(Fore.YELLOW + Style.BRIGHT + f"📦{start_path.name}")
    items = list(start_path.iterdir())
    for index, item in enumerate(items):
        connector = "├" if index < len(items) - 1 else "└"
        branch = Fore.BLACK + connector + Style.RESET_ALL
        vertical = Fore.BLACK + "│" + Style.RESET_ALL
        if item.is_dir():
            print(Fore.BLUE + f"{indent}{branch} 📂{item.name}")
            print_dir_structure(item, indent + f" {vertical} ", is_root=False)
        else:
            print(Fore.GREEN + f"{indent}{branch} 📜{item.name}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python script_name.py /path/to/directory")
        sys.exit(1)
    path = sys.argv[1]
    print_dir_structure(path)

if __name__ == "__main__":
    main()
