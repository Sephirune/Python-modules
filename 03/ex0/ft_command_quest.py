import sys
print("=== Command Quest ===")
if len(sys.argv) < 2:
    print("No arguments provided!")
    print("Program name: ft_command_quest.py")
    print("Total arguments: 1")
else:
    print("Program name: ft_command_quest.py")
    print(f"Arguments received: {len(sys.argv) - 1}")
    i: int = 1
    arg: str
    for arg in sys.argv[1:]:
        print(f"Argument {i}: {arg}")
        i += 1
    print(f"Total arguments: {len(sys.argv)}")
