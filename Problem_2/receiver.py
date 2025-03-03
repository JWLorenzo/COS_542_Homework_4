from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello from receiver"


@app.route("/hoppy")
def hoppy():
    return "hoppy happy"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
