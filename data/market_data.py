import requests
from datetime import datetime, timezone

def get_market_status():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin,ethereum",
        "vs_currencies": "usd",
        "include_24hr_change": "true"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        data = response.json()

        btc = data.get("bitcoin", {})
        eth = data.get("ethereum", {})

        return {
            "BTC": {
                "price": btc.get("usd", "unknown"),
                "change_24h": btc.get("usd_24h_change", "unknown")
            },
            "ETH": {
                "price": eth.get("usd", "unknown"),
                "change_24h": eth.get("usd_24h_change", "unknown")
            },
            "source": "coingecko",
            "updated_at_utc": datetime.now(timezone.utc).isoformat()
        }

    except Exception as e:
        return {
            "error": str(e),
            "source": "coingecko",
            "updated_at_utc": datetime.now(timezone.utc).isoformat()
        }
