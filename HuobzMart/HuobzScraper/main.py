import os
import requests
import shutil
import subprocess
from flask import Flask, request, jsonify
from bs4 import BeautifulSoup

app = Flask(__name__)

### 📌 Storage Paths ###
SCRAPER_FOLDER = os.path.expanduser("~/huobz/HuobzScraper")
WEBSITES_FOLDER = os.path.join(SCRAPER_FOLDER, "websites")
APPS_FOLDER = os.path.join(SCRAPER_FOLDER, "apps")

os.makedirs(WEBSITES_FOLDER, exist_ok=True)
os.makedirs(APPS_FOLDER, exist_ok=True)

### 🕸️ **Scrape Website Source Code** ###
@app.route('/api/scrape_website', methods=['POST'])
def scrape_website():
    data = request.json
    url = data.get("url")
    
    if not url.startswith("http"):
        url = f"http://{url}"

    domain = url.replace("http://", "").replace("https://", "").replace("/", "_")
    save_path = os.path.join(WEBSITES_FOLDER, domain)

    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        response.raise_for_status()

        # Save HTML content
        os.makedirs(save_path, exist_ok=True)
        with open(os.path.join(save_path, "index.html"), "w", encoding="utf-8") as f:
            f.write(response.text)

        # Extract and download assets (CSS, JS, Images)
        soup = BeautifulSoup(response.text, "html.parser")
        assets = {"css": [], "js": [], "images": []}

        for tag in soup.find_all(["link", "script", "img"]):
            src = tag.get("href") or tag.get("src")
            if src and not src.startswith("http"):
                src = url + src if src.startswith("/") else f"{url}/{src}"
            if src:
                file_type = "css" if "css" in src else "js" if "js" in src else "images"
                assets[file_type].append(src)

        # Download assets
        for file_type, urls in assets.items():
            os.makedirs(os.path.join(save_path, file_type), exist_ok=True)
            for file_url in urls:
                try:
                    r = requests.get(file_url, headers={'User-Agent': 'Mozilla/5.0'})
                    if r.status_code == 200:
                        filename = file_url.split("/")[-1]
                        with open(os.path.join(save_path, file_type, filename), "wb") as f:
                            f.write(r.content)
                except:
                    pass  # Skip failed downloads

        return jsonify({"message": "Website source code downloaded!", "saved_at": save_path})
    
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500


### 📱 **Download Android APK** ###
@app.route('/api/download_apk', methods=['POST'])
def download_apk():
    data = request.json
    app_name = data.get("app_name")

    if not app_name:
        return jsonify({"error": "Please provide app name!"}), 400

    apk_url = f"https://apkcombo.com/{app_name}/download/apk"
    save_path = os.path.join(APPS_FOLDER, f"{app_name}.apk")

    try:
        response = requests.get(apk_url, stream=True, headers={'User-Agent': 'Mozilla/5.0'})
        response.raise_for_status()

        with open(save_path, "wb") as f:
            shutil.copyfileobj(response.raw, f)

        return jsonify({"message": "APK downloaded!", "saved_at": save_path})
    
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500


### 🚀 **Run Server** ###
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
