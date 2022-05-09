from flask import Flask
from flask import session
import os

app = Flask(__name__)

i = 0

@app.route("/")
def index():
    global i
    i += 1
    return f"Hello, World! You are visitor #{i}, and I am {os.system(\"whoami\")}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
