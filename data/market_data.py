import requests

def get_market_status():
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

    response = requests.get(url)
    data = response.json()

    return {
        "symbol": data.get("symbol", "BTCUSDT"),
        "price": data.get("price", "unknown")
    }
