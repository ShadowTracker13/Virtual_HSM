# Virtual HSM — Hardware Security Module Simulation

A **Virtual Hardware Security Module (HSM)** that simulates real HSM behavior where cryptographic keys never leave the module boundary and applications request cryptographic operations through a secure API.

> Built for security hackathon demonstrations.

---

## Overview

A Hardware Security Module is a dedicated hardware device for managing cryptographic keys and performing crypto operations. This project simulates that architecture in software:

- **Keys never leave the HSM** — only operation results (ciphertext, signatures) are returned
- **All crypto operations** happen inside the module boundary
- **Policy engine** controls which operations are permitted
- **Authentication** is required before accessing any HSM function

---

## Architecture

```
Application / CLI (main.py)
        ↓
   HSM Core (hsm_core.py)
        ├── Authentication    (auth.py)
        ├── Policy Engine     (policy_engine.py)
        ├── Key Manager       (key_manager.py)
        └── Crypto Service    (crypto_service.py)
              ↓
      Secure Key Store (storage/keys.db)
```

---

## Project Structure

```
virtual-hsm/
├── README.md
├── requirements.txt
├── .gitignore
│
├── virtual_hsm/
│   ├── __init__.py
│   ├── main.py              # CLI interface
│   ├── hsm_core.py          # Central HSM controller
│   ├── auth.py              # SHA-256 authentication
│   ├── key_manager.py       # Key generation & storage
│   ├── crypto_service.py    # AES-GCM & RSA-PSS operations
│   ├── policy_engine.py     # Operation policy rules
│   │
│   └── storage/
│       └── keys.db          # SQLite key store (auto-created)
│
└── .venv/
```

---

## Modules

| Module | Responsibility |
|--------|---------------|
| `auth.py` | SHA-256 password authentication with 3-attempt lockout |
| `key_manager.py` | AES-256 / RSA-2048 key generation, SQLite storage |
| `crypto_service.py` | AES-GCM encrypt/decrypt, RSA-PSS sign/verify |
| `policy_engine.py` | Rule-based operation access control |
| `hsm_core.py` | Central controller — enforces policy, delegates operations |
| `main.py` | Interactive CLI menu |

---

## Installation

```bash
# Clone the repository
git clone https://github.com/ShadowTracker13/secure-vault.git
cd secure-vault

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## Usage

```bash
python -m virtual_hsm.main
```

**Default password:** `admin123`

### CLI Menu

```
Virtual HSM System

  1 │ Generate AES Key
  2 │ Generate RSA Key
  3 │ Encrypt Data
  4 │ Decrypt Data
  5 │ Sign Data
  6 │ Verify Signature
  7 │ Exit
```

### Demo Workflow

1. **Start** → Authenticate with password
2. **Generate AES Key** → Receive key ID (key material stays sealed)
3. **Encrypt Data** → Provide key ID + plaintext → Get ciphertext
4. **Decrypt Data** → Provide key ID + ciphertext → Get plaintext
5. **Generate RSA Key** → Receive key ID
6. **Sign Data** → Provide key ID + data → Get signature
7. **Verify Signature** → Provide key ID + data + signature → Get result

---

## Security Model

- 🔒 **Keys never leave the HSM** — only key IDs are returned to the user
- 🔐 **AES-256-GCM** for authenticated encryption
- ✍️ **RSA-2048 PSS** for digital signatures
- 🛡️ **Policy engine** prevents unauthorized operations
- 🔑 **SQLite key store** — keys stored as BLOBs, never printed

---

## Technologies

- Python 3
- `cryptography` — AES-GCM, RSA-PSS
- `sqlite3` — Secure key storage
- `hashlib` — SHA-256 authentication

---

## License

MIT
