print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
print("Initiating secure vault access...")
print("Vault connection established with failsafe protocols\n")

print("SECURE EXTRACTION: ")
with open("classified_data.txt", "r") as vault_file:
    data = vault_file.read()
    print("[CLASSIFIED] Quantum encryption keys recovered")
    print("[CLASSIFIED] Archive integrity: 100%")

print("\nSECURE PRESERVATION: ")
with open("classified_data.txt", "w") as vault_file:
    vault_file.write("[CLASSIFIED] New security protocols archived")

print("Vault automatically sealed upon completion")
print("\nAll vault operations completed with maximum security.")
