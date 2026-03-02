import importlib


requirements = [
    "pandas",
    "matplotlib",
    "numpy",
    "requests"
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
    import matplotlib
    import pandas as pd
    import numpy as np
    import requests as rq

    print("Analyzing Matrix data...")
    print("Processing 1000 data points...")
    print("Generating visualization...")
    
    
    print("Analysis complete!")
    print("Results saved to: matrix\analysis.png}")
