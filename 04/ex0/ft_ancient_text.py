print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")

try:
    file = open("ancient_fragment.txt")
except Exception:
    file = None
if not file:
    print("ERROR: Storage vault not found. Run data generator first.")
else:
    print("Accessing Storage Vault: ancient_fragment.txt")
    print("Connection established...\n")

    print(file.read())

    print("\nData recovery complete. Storage unit disconnected")
    file.close()
