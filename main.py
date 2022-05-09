from flask import Flask

app = Flask(__name__)

visitors = 0

@app.route("/")
def index():
    visitors += 1
    return f"Hello, World! You are visitor #{visitors}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
