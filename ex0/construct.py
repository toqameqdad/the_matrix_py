import os
import site
import sys


def is_virtual_environment() -> bool:
    return sys.prefix != sys.base_prefix


def get_environment_name() -> str:
    return os.path.basename(sys.prefix)


def get_first_site_package() -> str:
    paths = site.getsitepackages()

    if not paths:
        return "Unknown"

    return paths[0]


def show_outside_matrix() -> None:
    print("Outside the Matrix")
    print("MATRIX STATUS: You’re still plugged in")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print(f"Global Python Prefix: {sys.base_prefix}")
    print("Global package installation path:")
    print(get_first_site_package())
    print("WARNING: You’re in the global environment!")
    print("The machines can see everything you install.")
    print()
    print("To enter the construct, run:")
    print("python3 -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print(r"matrix_env\Scripts\activate # On Windows")
    print("Then run this program again.")


def show_inside_construct() -> None:
    print("Inside the Construct")
    print("MATRIX STATUS: Welcome to the construct")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {get_environment_name()}")
    print(f"Environment Path: {sys.prefix}")
    print(f"Global Python Prefix: {sys.base_prefix}")
    print("SUCCESS: You’re in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.")
    print("Package installation path:")
    print(get_first_site_package())


def main() -> None:
    if is_virtual_environment():
        show_inside_construct()
    else:
        show_outside_matrix()


if __name__ == "__main__":
    main()
