import requests
from datetime import datetime, timezone

def get_market_status():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin,ethereum",
        "vs_currencies": "usd",
        "include_24hr_change": "true"
    }

    response = requests.get(url, params=params, timeout=10)
    data = response.json()

    return {
        "BTC": {
            "price": data.get("bitcoin", {}).get("usd", "unknown"),
            "change_24h": data.get("bitcoin", {}).get("usd_24h_change", "unknown")
        },
        "ETH": {
            "price": data.get("ethereum", {}).get("usd", "unknown"),
            "change_24h": data.get("ethereum", {}).get("usd_24h_change", "unknown")
        },
        "source": "coingecko",
        "updated_at_utc": datetime.now(timezone.utc).isoformat()
    }
