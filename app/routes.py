from flask import (
    Flask, 
    render_template
)
import requests

BACKEND_URL = "http://127.0.0.1:5000"

app = Flask(__name__)

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/about")
def get_about_page():
    out = {
        "up": False
    }
    ping_url = "%s/%s" % (BACKEND_URL, "ping")
    up = requests.get(ping_url)
    if up.status_code == 200:
        out["up"] = True
        version_url = "%s/%s" % (BACKEND_URL, "Version")
        version_response = requests.get(version_url)
        version_json = version_response.json()
        out["version"] = version_json.get("version")
    return render_template("about.html", content=out)