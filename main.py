from flask import Flask
from flask import session
import subprocess

app = Flask(__name__)

i = 0

@app.route("/")
def index():
    global i
    i += 1
    name = subprocess.run(["whoami"], capture_output=True).stdout.decode("utf-8")
    return f"Hello, World! You are visitor #{i}, and I am {name}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
