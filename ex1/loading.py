import importlib
import sys
from types import ModuleType
from typing import Optional


REQUIRED_PACKAGES: dict[str, str] = {
    "pandas": "Data manipulation ready",
    "numpy": "Numerical computation ready",
    "matplotlib": "Visualization ready",
}


def load_package(package_name: str) -> Optional[ModuleType]:
    try:
        return importlib.import_module(package_name)
    except ImportError:
        return None


def check_dependencies() -> bool:
    print("Checking dependencies:")
    all_available = True

    for package_name, description in REQUIRED_PACKAGES.items():
        module = load_package(package_name)

        if module is None:
            print(f"[MISSING] {package_name} - install required")
            all_available = False
        else:
            version = getattr(module, "__version__", "unknown")
            print(f"[OK] {package_name} ({version}) - {description}")

    return all_available


def print_installation_help() -> None:
    print()
    print("Some dependencies are missing.")
    print("Install them using pip:")
    print("pip install -r requirements.txt")
    print()
    print("Or using Poetry:")
    print("poetry install")
    print("poetry run python loading.py")


def compare_dependency_managers() -> None:
    print()
    print("Dependency management comparison:")
    print("pip: installs packages listed in requirements.txt")
    print("Poetry: manages dependencies using pyproject.toml")
    print("pip is simple and direct.")
    print("Poetry provides project isolation and lock files.")


def analyze_matrix_data() -> None:
    pandas = load_package("pandas")
    numpy = load_package("numpy")
    pyplot_module = importlib.import_module("matplotlib.pyplot")

    if pandas is None or numpy is None:
        raise RuntimeError("Required packages are not available.")

    print()
    print("Analyzing Matrix data...")

    signal_strength = numpy.random.normal(loc=75, scale=10, size=1000)
    anomaly_score = numpy.random.normal(loc=30, scale=8, size=1000)

    data_frame = pandas.DataFrame(
        {
            "signal_strength": signal_strength,
            "anomaly_score": anomaly_score,
        }
    )

    print(f"Processing {len(data_frame)} data points...")

    average_signal = data_frame["signal_strength"].mean()
    average_anomaly = data_frame["anomaly_score"].mean()

    print(f"Average signal strength: {average_signal:.2f}")
    print(f"Average anomaly score: {average_anomaly:.2f}")

    print("Generating visualization...")

    pyplot_module.figure()
    pyplot_module.scatter(
        data_frame["signal_strength"],
        data_frame["anomaly_score"],
        alpha=0.5,
    )
    pyplot_module.title("Matrix Data Analysis")
    pyplot_module.xlabel("Signal Strength")
    pyplot_module.ylabel("Anomaly Score")
    pyplot_module.savefig("matrix_analysis.png")
    pyplot_module.close()

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    print("LOADING STATUS: Loading programs...")

    dependencies_ready = check_dependencies()
    compare_dependency_managers()

    if not dependencies_ready:
        print_installation_help()
        sys.exit(1)

    analyze_matrix_data()


if __name__ == "__main__":
    main()
