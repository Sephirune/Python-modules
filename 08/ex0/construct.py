import sys
import os
import site


def checker() -> int:
    if sys.prefix != sys.base_prefix:
        return 1
    else:
        return 0


def sys_info() -> None:
    print("MATRIX STATUS: You're still plugged in")
    print(f"\nCurrent Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print("\nWARNING: You're in the global environment!")
    print("The machines can see everything you install.\n")
    print(
     'To enter the construct, run:',
     '\npython -m venv matrix_env',
     '\nsource matrix_env/bin/activate # On Unix',
     '\nmatrix_env',
     '\nScripts',
     '\nactivate # On Windows'
     )


def in_env() -> None:
    env_path: str = sys.prefix
    env_name: str = os.path.basename(sys.prefix)
    print("MATRIX STATUS: Welcome to the construct\n")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {env_path}")
    print(f"Environment Path: {env_name}")

    print(
        "\nSuccess: You're in an isolated environment!",
        '\nSafe to install packages without affecting',
        '\nthe global system.'
        )

    print("Package installation path:")
    path: list[str] = site.getsitepackages()
    print(path[0])


def main() -> None:
    if checker():
        in_env()
    else:
        sys_info()


main()
