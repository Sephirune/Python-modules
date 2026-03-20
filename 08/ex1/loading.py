import importlib


requirements: list = [
    "pandas",
    "matplotlib",
    "numpy",
]


def checker() -> list:
    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")

    loaded_modules: dict = {}

    for pkg in requirements:
        try:
            module = importlib.import_module(pkg)
            version = getattr(module, "__version__", "unknown_ver")
            print(f"[OK] {pkg} ({version}) - ready")
            loaded_modules[pkg] = module

        except ImportError:
            print(f"Missing {pkg}!\n")
            print("Please, refer to the install instructions.")

    return loaded_modules


def analyze_matrix() -> None:
    import matplotlib.pyplot as plt
    import pandas as pd
    import numpy as np

    print("Analyzing Matrix data...")
    print("Processing 1000 data points...")
    print("Generating visualization...")

    data = np.random.normal(loc=0, scale=1, size=1000)
    df = pd.DataFrame({"matrix_signal": data})

    plt.style.use("dark_background")
    plt.hist(df["matrix_signal"], bins=30, color="#DF346D")
    plt.title("Matrix data signal analysis")
    plt.xlabel('Signal')
    plt.ylabel('Frequency')
    plt.text(
        x=0,
        y=20,
        s="SLAY",
        fontsize=100,
        color="#FFFB00",
        ha="center",
        va="center"
    )
    plt.savefig("matrix_analysis.png")
    plt.show()

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    modules: list = checker()
    if len(modules) < len(requirements):
        return

    analyze_matrix()


if __name__ == "__main__":
    main()
