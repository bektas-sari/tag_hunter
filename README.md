# 🕷️ TagHunter (Flask web App)

**Tag Hunter** is a minimalist web scraping tool built with Flask, Selenium, and BeautifulSoup. It allows users to input any publicly accessible URL, automatically detect all HTML tags on the page, and select which tag's content to extract.

---

## 🚀 Features

* 🧭 Enter any URL and parse it dynamically with Selenium
* 🔍 Automatically detects all unique HTML tags in the page
* 🧠 Preview content for each HTML tag before scraping
* 📋 Copy extracted content to clipboard
* ⬇️ Export scraped content as `.txt`
* 🎨 Clean, responsive and beginner-friendly interface

---

## 🧰 Built With

* [Python](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/)
* [Selenium](https://www.selenium.dev/)
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
* HTML/CSS (Minimalist UI)

---

## 📦 Installation

```bash
git clone https://github.com/bektas-sari/taghunter.git
cd taghunter
pip install -r requirements.txt
python app.py
```

> Visit `http://localhost:5000` in your browser.

Make sure you have:

* Python 3.8+
* Google Chrome installed
* ChromeDriver compatible with your Chrome version

---

## 🖥️ Project Structure

```
taghunter/
├── app.py
├── requirements.txt
├── templates/
│   ├── index.html
│   ├── select.html
│   └── result.html
├── static/
│   └── style.css
└── README.md
```

---

## 👤 Developer

**Bektas Sari**
Email: [bektas.sari@gmail.com](mailto:bektas.sari@gmail.com) 
GitHub: [bektas-sari](https://github.com/bektas-sari)
LinkedIn: [linkedin.com/in/bektas-sari](https://www.linkedin.com/in/bektas-sari)
ResearchGate: [Bektas Sari](https://www.researchgate.net/profile/Bektas-Sari-3)
Academia: [Academia.edu](https://independent.academia.edu/bektassari)

---

## 📄 License

This project is licensed under the MIT License.
