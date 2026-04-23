from flask import Flask
from data.market_data import get_market_status

app = Flask(__name__)

@app.route("/")
def home():
    return "Trading system is running 🚀"

@app.route("/market")
def market():
    return get_market_status()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
