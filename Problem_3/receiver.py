from flask import Flask
import requests

app = Flask(__name__)


@app.route("/")
def index():
    try:
        response = requests.get("http://receiver1:5002/")
        return f"Got this from receiver 1: {response.text}"
    except requests.exceptions.RequestException as e:
        return f"error: {str(e)}"


@app.route("/hoppy")
def hoppy():
    return "hoppy happy"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
