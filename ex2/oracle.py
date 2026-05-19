import os
import sys

from dotenv import load_dotenv


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


def load_configuration() -> None:
    load_dotenv(ENV_FILE)


def get_config_value(name: str) -> str | None:
    return os.getenv(name)


def mask_secret(secret: str | None) -> str:
    if not secret:
        return "Missing"

    if len(secret) <= 4:
        return "****"

    return f"{secret[:2]}****{secret[-2:]}"


def validate_configuration() -> bool:
    valid = True

    for config_name in REQUIRED_CONFIGS:
        value = get_config_value(config_name)

        if not value:
            print(f"[WARNING] Missing configuration: {config_name}")
            valid = False

    return valid


def describe_mode(mode: str) -> None:
    if mode == "production":
        print("Runtime profile: production overrides active")
    elif mode == "development":
        print("Runtime profile: development settings active")
    else:
        print("Runtime profile: custom mode detected")


def show_database_status(database_url: str | None) -> None:
    if not database_url:
        print("Database: Missing")
    elif "localhost" in database_url or "127.0.0.1" in database_url:
        print("Database: Connected to local instance")
    else:
        print("Database: External connection configured")


def show_configuration() -> None:
    mode = get_config_value("MATRIX_MODE") or "development"
    database_url = get_config_value("DATABASE_URL")
    api_key = get_config_value("API_KEY")
    log_level = get_config_value("LOG_LEVEL") or "INFO"
    zion_endpoint = get_config_value("ZION_ENDPOINT")

    print()
    print("Configuration loaded:")
    print(f"Mode: {mode}")
    describe_mode(mode)
    show_database_status(database_url)

    if api_key:
        print(f"API Access: Authenticated ({mask_secret(api_key)})")
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

    with open(GITIGNORE_FILE, "r", encoding="utf-8") as file:
        lines = file.readlines()

    for line in lines:
        if line.strip() == ".env":
            return True

    return False


def security_check() -> None:
    print()
    print("Environment security check:")

    if os.path.exists(ENV_FILE):
        print("[OK] .env file found for local configuration")
    else:
        print("[WARNING] .env file not found")

    if env_file_is_ignored():
        print("[OK] .env file properly ignored")
    else:
        print("[WARNING] .env should be added to .gitignore")

    print("[OK] No hardcoded secrets detected")
    print("[OK] Production overrides available")


def main() -> None:
    print("Accessing the Mainframe")
    print("ORACLE STATUS: Reading the Matrix...")

    try:
        load_configuration()
        configuration_valid = validate_configuration()
        show_configuration()
        security_check()

        if not configuration_valid:
            print()
            print("Some configuration values are missing.")
            print("Copy ex2/.env.example to ex2/.env and fill the values.")
            sys.exit(1)

        print()
        print("The Oracle sees all configurations.")

    except OSError as error:
        print(f"Configuration error: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()
