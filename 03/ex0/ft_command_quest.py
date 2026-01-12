import sys
print("=== Command Quest ===")
if len(sys.argv) == 1:
    print("No arguments provided!")
    print("Program name: ft_command_quest.py")
    print(f"Total arguments: 1")
else:
    print("Program name: ft_command_quest.py")
    print(f"Arguments received: {len(sys.argv)}")
    for data in sys.argv:
        print(f"Argument 1: {data}")
    print(f"Total arguments: {len(sys.argv)}")