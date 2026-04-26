import requests

def get_market_status():
    url = "https://api.binance.com/api/v3/ticker/price"
    params = {"symbol": "BTCUSDT"}

    response = requests.get(url, params=params, timeout=10)
    data = response.json()

    return {
        "symbol": data.get("symbol", "BTCUSDT"),
        "price": data.get("price", "unknown"),
        "raw": data
    }
