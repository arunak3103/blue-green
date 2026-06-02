from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Blue Green Deployment V2"

app.run(host="0.0.0.0", port=80)