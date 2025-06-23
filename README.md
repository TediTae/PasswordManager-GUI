# 🔐 Password Manager - GUI App with Python & Tkinter

A beginner-friendly and functional **Password Manager** developed using **Python** and **Tkinter**.  
It allows you to:
- Generate strong, random passwords
- Copy them instantly to clipboard
- Save your credentials locally in a text file

This project is ideal for beginners who are learning GUI programming and want to build something practical and secure (with basic measures).

---

## 🚀 Features

- 🔐 **Random Password Generator**  
  Includes uppercase/lowercase letters, numbers, and symbols.

- 📋 **Clipboard Copy**  
  Generated passwords are instantly copied to your clipboard using `pyperclip`.

- 📝 **Local Data Storage with JSON**  
  Credentials are now saved in `data.json` using a structured, expandable format.

- 🔍 **Website-Based Password Search**  
  You can now search for stored credentials by entering a website name.  
  If found, the username and password are displayed — and the password is copied to clipboard automatically.

- ⚠️ **Empty Field Detection**  
  Warns the user if any input field is left blank.

---

## 🧰 Technologies Used

- Python 3.x  
- Tkinter  
- Pyperclip  
- Built-in `random` module

---

## 📦 Installation
1. Clone the repository
2. pip install pyperclip
3. Choose a desired logo for your GUI and make sure you have a file named logo.png in the same directory.
4. run main.py

---

## 🛡️ Security Note
- This project is made for educational purposes.
- Storing passwords in plain text is not secure. Consider using encryption (e.g., with cryptography or hashing) before using this in real-world scenarios.

---

## 🧠 Future Improvements
- ✅ Convert data storage to JSON format *(Completed ✅)*
- 🔍 Add password search by website *(Completed ✅)*
- 🔐 Encrypt saved credentials
- 🌙 Dark mode / light mode switch
- 💾 Use database (e.g. SQLite) for advanced storage

---

## 🤝 Contributing
- Pull requests and feedback are welcome. If you spot a bug or want to improve something, feel free to contribute!

## 📜 License
- MIT License © 2025

## Contact
- tolgayilmaz1377@gmail.com
