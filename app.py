from flask import Flask, render_template, request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from flask import Response

app = Flask(__name__)

def ensure_http(url):
    """Ensure the URL starts with http:// or https://"""
    if not url.startswith("http://") and not url.startswith("https://"):
        return "http://" + url
    return url

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = ensure_http(request.form['url'])

        try:
            service = Service()
            options = webdriver.ChromeOptions()
            options.add_argument("--headless")
            driver = webdriver.Chrome(service=service, options=options)

            driver.get(url)
            time.sleep(2)
            page_source = driver.page_source
            driver.quit()

            soup = BeautifulSoup(page_source, 'html.parser')
            tags = list(set(tag.name for tag in soup.find_all()))

            # Tag önizlemeleri
            samples = {}
            for tag in tags:
                el = soup.find(tag)
                if el and el.get_text(strip=True):
                    samples[tag] = el.get_text(strip=True)
                else:
                    samples[tag] = "(no preview)"

            return render_template('select.html', url=url, tags=sorted(tags), samples=samples)

        except Exception as e:
            return f"<h3>Error loading the page: {e}</h3>"

    return render_template('index.html')
    if request.method == 'POST':
        url = ensure_http(request.form['url'])

        try:
            # Start Selenium
            service = Service()
            options = webdriver.ChromeOptions()
            options.add_argument("--headless")  # Arka planda çalışsın
            driver = webdriver.Chrome(service=service, options=options)

            driver.get(url)
            time.sleep(2)  # Sayfa yüklemesi için bekle
            page_source = driver.page_source
            driver.quit()

            soup = BeautifulSoup(page_source, 'html.parser')
            # Sayfadaki tüm benzersiz HTML tag'lerini bul
            tags = list(set(tag.name for tag in soup.find_all()))
            return render_template('select.html', url=url, tags=sorted(tags))

        except Exception as e:
            return f"<h3>Error loading the page: {e}</h3>"

    return render_template('index.html')


@app.route('/download/<tag>')
def download_txt(tag):
    content = request.args.get('data')
    if not content:
        return "No data provided."
    return Response(
        content,
        mimetype="text/plain",
        headers={"Content-Disposition": f"attachment;filename=scraped_{tag}.txt"}
    )


@app.route('/scrape', methods=['POST'])
def scrape():
    url = ensure_http(request.form['url'])
    selected_tag = request.form['tag']

    try:
        service = Service()
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(service=service, options=options)

        driver.get(url)
        time.sleep(10)
        page_source = driver.page_source
        driver.quit()

        soup = BeautifulSoup(page_source, 'html.parser')
        elements = soup.find_all(selected_tag)
        content = [el.get_text(strip=True) for el in elements if el.get_text(strip=True)]

        return render_template('result.html', content=content, tag=selected_tag)

    except Exception as e:
        return f"<h3>Error scraping the page: {e}</h3>"

if __name__ == '__main__':
    app.run(debug=True)
