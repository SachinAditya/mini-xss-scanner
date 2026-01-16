# 🛡 Mini XSS Scanner

Lightweight reflected XSS scanner for educational and authorized web security testing.

---

## ✨ Features

- Detects reflected XSS vulnerabilities
- Scans URL parameters automatically
- Simple command-line interface
- Lightweight and fast
- Open-source (MIT License)

---

## ⚙️ Installation

```bash
git clone https://github.com/SachinAditya/mini-xss-scanner.git
cd mini-xss-scanner
pip install -r requirements.txt
```

---

## 🚀 Usage

```bash
python scanner.py -u "http://testphp.vulnweb.com/search.php?test=query"
```

---

## 📌 Example Output

```
[+] XSS FOUND in parameter: test
Payload: <script>alert(1)</script>
```

---

## ⚠️ Disclaimer

This tool is created for **educational purposes and authorized security testing only**.  
Do NOT use this tool against systems you do not own or have explicit permission to test.

---

## 📄 License

MIT License

---

## 👤 Author

Sachin Vishwakarma (SachinAditya)
