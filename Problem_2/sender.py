from flask import Flask
import requests


app = Flask(__name__)


@app.route("/")
def hello():
    try:
        response = requests.get("http://receiver:5001/")
        return f"received this from receiver: {response.text}"
    except requests.exceptions.RequestException as e:
        return f"error: {str(e)}"


@app.route("/buya")
def buya():
    try:
        response = requests.get("http://receiver:5001/hoppy")
        return f"is hoppy happy today? : {response.text}"
    except requests.exceptions.RequestException as e:
        return f"error: {str(e)}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
