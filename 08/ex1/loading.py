import importlib


requirements = [
    "pandas",
    "matplotlib",
    "numpy",
]


def checker() -> list:
    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")

    loaded_modules = {}

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


def analyze_matrix():
    import matplotlib.pyplot as plt
    import pandas as pd
    import numpy as np

    print("Analyzing Matrix data...")
    print("Processing 1000 data points...")
    print("Generating visualization...")

    data = np.random.normal(loc=0, scale=1, size=1000)
    df = pd.DataFrame({"matrix_signal": data})

    plt.style.use("dark_background")
    plt.hist(df["matrix_signal"], bins=30, color='lime')
    plt.title("Matrix data signal analysis")
    plt.xlabel('Signal')
    plt.ylabel('Frequency')
    plt.savefig("matrix_analysis.png")
    plt.show()

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


def main():
    modules = checker()
    if len(modules) < len(requirements):
        return

    analyze_matrix()


main()
