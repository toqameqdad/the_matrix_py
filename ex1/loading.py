import importlib
import sys


REQUIRED_PACKAGES: dict[str, str] = {
    "pandas": "Data manipulation ready",
    "numpy": "Numerical computation ready",
    "matplotlib": "Visualization ready",
}


def load_package(package_name: str) -> object | None:
    try:
        return importlib.import_module(package_name)
    except ImportError:
        return None


def get_package_version(module: object) -> str:
    version = getattr(module, "__version__", "unknown")
    return str(version)


def check_dependencies() -> bool:
    print("Checking dependencies:")
    all_available = True

    for package_name, description in REQUIRED_PACKAGES.items():
        module = load_package(package_name)

        if module is None:
            print(f"[MISSING] {package_name} - install required")
            all_available = False
        else:
            version = get_package_version(module)
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
    pyplot = load_package("matplotlib.pyplot")

    if pandas is None or numpy is None or pyplot is None:
        raise RuntimeError("Required packages are not available.")

    print()
    print("Analyzing Matrix data...")

    numpy_random = getattr(numpy, "random")
    normal = getattr(numpy_random, "normal")

    signal_strength = normal(loc=75, scale=10, size=1000)
    anomaly_score = normal(loc=30, scale=8, size=1000)

    data_frame_class = getattr(pandas, "DataFrame")
    data_frame = data_frame_class(
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

    figure = getattr(pyplot, "figure")
    scatter = getattr(pyplot, "scatter")
    title = getattr(pyplot, "title")
    xlabel = getattr(pyplot, "xlabel")
    ylabel = getattr(pyplot, "ylabel")
    savefig = getattr(pyplot, "savefig")
    close = getattr(pyplot, "close")

    figure()
    scatter(
        data_frame["signal_strength"],
        data_frame["anomaly_score"],
        alpha=0.5,
    )
    title("Matrix Data Analysis")
    xlabel("Signal Strength")
    ylabel("Anomaly Score")
    savefig("matrix_analysis.png")
    close()

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
