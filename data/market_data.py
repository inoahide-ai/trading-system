import requests
from datetime import datetime, timezone

def get_market_status():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin",
        "vs_currencies": "usd"
    }

    response = requests.get(url, params=params, timeout=10)
    data = response.json()

    return {
        "symbol": "BTCUSD",
        "price": data.get("bitcoin", {}).get("usd", "unknown"),
        "source": "coingecko",
        "updated_at_utc": datetime.now(timezone.utc).isoformat()
    }
