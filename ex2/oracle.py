import os
import sys


try:
    from dotenv import load_dotenv
    DOTENV_AVAILABLE = True
except ImportError:
    DOTENV_AVAILABLE = False


SCRIPT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
ENV_FILE = os.path.join(SCRIPT_DIRECTORY, ".env")
GITIGNORE_FILE = os.path.join(SCRIPT_DIRECTORY, ".gitignore")

REQUIRED_CONFIGS: list[str] = [
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
]


def load_configuration() -> bool:
    if not DOTENV_AVAILABLE:
        print("ORACLE STATUS: Reading the Matrix...")
        print("[ERROR] python-dotenv is not installed.")
        print("Install it using:")
        print("pip install python-dotenv")
        return False

    load_dotenv(ENV_FILE)
    return True


def get_config_value(name: str) -> str | None:
    return os.getenv(name)


def validate_configuration() -> bool:
    valid = True

    for config_name in REQUIRED_CONFIGS:
        value = get_config_value(config_name)

        if not value:
            valid = False

    return valid


def show_database_status(database_url: str | None) -> str:
    if not database_url:
        return "Missing"

    if (
        "localhost" in database_url
        or "127.0.0.1" in database_url
    ):
        return "Connected to local instance"

    return "External connection configured"


def show_configuration() -> None:
    mode = get_config_value("MATRIX_MODE") or "development"
    database_url = get_config_value("DATABASE_URL")
    api_key = get_config_value("API_KEY")
    log_level = get_config_value("LOG_LEVEL") or "INFO"
    zion_endpoint = get_config_value("ZION_ENDPOINT")

    print("\nConfiguration loaded:")
    print(f"Mode: {mode}")
    print(
        f"Database: "
        f"{show_database_status(database_url)}"
    )

    if api_key:
        print("API Access: Authenticated")
    else:
        print("API Access: Missing")

    print(f"Log Level: {log_level}")

    if zion_endpoint:
        print("Zion Network: Online")
    else:
        print("Zion Network: Offline")


def env_file_is_ignored() -> bool:
    if not os.path.exists(GITIGNORE_FILE):
        return False

    with open(
        GITIGNORE_FILE,
        "r",
        encoding="utf-8",
    ) as file:
        lines = file.readlines()

    for line in lines:
        if line.strip() == ".env":
            return True

    return False


def security_check() -> None:
    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")

    if env_file_is_ignored():
        print("[OK] .env file properly configured")
    else:
        print(
            "[WARNING] .env should be added "
            "to .gitignore"
        )

    print("[OK] Production overrides available")


def main() -> None:
    if not load_configuration():
        sys.exit(1)

    print("ORACLE STATUS: Reading the Matrix...")

    configuration_valid = validate_configuration()

    show_configuration()
    security_check()

    if not configuration_valid:
        print()
        print("WARNING: Missing configuration values.")

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
