
# Security Project

A security-based Python project with:
- Log analysis  
- File encryption & decryption  
- Simple Windows cleanup script

---

## Folder Structure

```

security-project/
├── logs/
│   └── sample.log
├── analyzer.py
├── encrypt.py
├── decrypt.py
├── cleanup.bat
├── requirements.txt
└── README.md

```

---

## How to Run

### Install dependencies
```

pip install -r requirements.txt

```

### 1. Analyze logs
```

python analyzer.py

```

### 2. Encrypt report
```

python encrypt.py

```

### 3. Decrypt report
```

python decrypt.py

```

### 4. Cleanup logs (Windows)
```

cleanup.bat

```

---

## Notes
- `key.key` and log files are ignored using `.gitignore`.
- Output files (`report.txt`, `.enc`, decrypted file) are also ignored.

---

## Author
Kammari Vijaya Tejaswini



