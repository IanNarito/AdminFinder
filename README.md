# 🔐 Admin Panel Finder (CLI Tool)

A clean and customizable Python CLI tool for scanning websites to find potential admin login panels.  
Designed for red teamers, bug bounty hunters, and curious minds.

---

## 🚀 Features

- Fast and simple admin panel scanner
- Default wordlist included (can also use custom wordlists)
- Random User-Agent for every scan
- Clean CLI output with color-coded results
- Gracefully handles `Ctrl + C` interruption
- Zero dependencies outside the basics

---

## 🧑‍💻 Installation

> 🐍 Python 3.6+ is required

1. **Clone the repo**
```bash
git clone https://github.com/yourname/admin-finder.git
cd admin-finder
pip install -r requirements.txt
python3 main.py --url https://example.com
