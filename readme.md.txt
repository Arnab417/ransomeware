# 🔐 Desktop File Locker (Totally Not Ransomware)

## 🚨 Disclaimer
**This is for educational purposes only, you absolute rebel.** If you use this irresponsibly, I’m not bailing you out of jail. Use it ethically, or enjoy the consequences. Seriously, don't be that person.

## 🔥 Overview
This masterpiece consists of two scripts:
1. **lock_files.py** – Holds your Desktop files hostage (just for fun, of course).
2. **unlock_files.py** – Releases the hostages, assuming you actually want them back.

Oh, and because I'm *so* nice, I’ve also included precompiled `.exe` files, so you don’t even need Python to destroy your own files. One click, and boom—chaos unleashed.

## ⚠️ Warning
Running `lock_files.py` will mercilessly encrypt everything on your Desktop. If you don’t have the decryption key, well… good luck explaining that to your future self. 

## 📌 Features
- Turns all your precious Desktop files into unreadable gibberish (except this script, because even chaos has rules).
- Brings them back from the abyss with the correct key.
- Uses **Fernet encryption** (fancy, right?).
- Pops up a delightful message box to inform you of your digital destruction.
- Locks files in read-only mode because why not make it extra annoying?
- Now includes `.exe` versions because I love making things even easier for you (and more dangerous for your files).

## 📂 File Structure
```
📁 Desktop Locker
│-- lock_files.py   # Encrypts your files (oops?)
│-- unlock_files.py # Saves your butt
│-- lock_files.exe  # Same chaos, but no Python required
│-- unlock_files.exe # Rescue operation, now with fewer clicks
```

## 🛠️ Installation & Usage
### Running the `.exe` Files (No Dependencies Needed!)
If you don’t want to deal with installing Python or dependencies (because who has time for that?), just use the `.exe` files like a true efficiency expert:

- **To lock files:**
  - Double-click `lock_files.exe`
  - Watch your Desktop files disappear into encryption oblivion
  - Enjoy the panic

- **To unlock files:**
  - Double-click `unlock_files.exe`
  - Hope you actually want your files back
  - Breathe a sigh of relief (or not)

Absolutely no setup required—just download and run like the reckless genius you are. The `.exe` files were built using **PyInstaller**, so they work out of the box without any additional installation. Just click and let the mayhem begin!

### Running the Python Scripts (For the Masochists)
If you insist on using the scripts instead of the convenient `.exe` files, here’s what you need:

#### Prerequisites
- Python 3 (because we’re not cavemen)
- Install dependencies:
  ```bash
  pip install cryptography
  ```

#### Running the Encryption Script (Lock Files)
```bash
python lock_files.py
```

#### Running the Decryption Script (Unlock Files)
```bash
python unlock_files.py
```

## 🛡️ How It Works
- Uses a **hardcoded key** (because why not make security experts cry?).
- Scans your Desktop like a digital vulture.
- Encrypts files and slaps a `.locked` extension on them.
- The decryption script undoes the chaos, assuming you run it before a panic attack.

## ⚠️ Legal & Ethical Considerations
This is a **learning tool**, not your personal chaos generator. If you use this for anything shady, don’t expect me to visit you in prison. Also, I don’t do tech support for self-inflicted disasters.

## 🛠️ Author
Created by **arnab417**, your friendly neighborhood cyber troublemaker.

---
Use responsibly, or don’t—I’m not your parent. 🚀

