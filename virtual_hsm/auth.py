"""
Virtual HSM — Authentication Module
SHA-256 password authentication for HSM access control.
"""

import hashlib
import getpass

# Default password hash (admin123)
DEFAULT_PASSWORD_HASH = hashlib.sha256("admin123".encode()).hexdigest()

# In-memory store — in production this would be persisted
_password_hash = DEFAULT_PASSWORD_HASH


def _hash_password(password: str) -> str:
    """Hash a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()


def authenticate() -> bool:
    """
    Prompt the user for a password and authenticate.
    Returns True if credentials are valid, False otherwise.
    """
    print("\n╔══════════════════════════════════════╗")
    print("║     Virtual HSM — Authentication     ║")
    print("╚══════════════════════════════════════╝")
    
    max_attempts = 3
    for attempt in range(1, max_attempts + 1):
        password = getpass.getpass(f"  Enter HSM password (attempt {attempt}/{max_attempts}): ")
        if _hash_password(password) == _password_hash:
            print("  ✓ Authentication successful.\n")
            return True
        else:
            print(f"  ✗ Invalid password.")
    
    print("  ✗ Maximum attempts exceeded. Access denied.\n")
    return False


def change_password(old_password: str, new_password: str) -> bool:
    """Change the HSM password."""
    global _password_hash
    if _hash_password(old_password) == _password_hash:
        _password_hash = _hash_password(new_password)
        print("  ✓ Password changed successfully.")
        return True
    print("  ✗ Old password is incorrect.")
    return False
