import requests
from config import BTC_PRICE_API, HTTP_TIMEOUT


def get_btc_price_eur():
    resp = requests.get(
        BTC_PRICE_API,
        params={"ids": "bitcoin", "vs_currencies": "eur"},
        timeout=HTTP_TIMEOUT,
    )
    resp.raise_for_status()
    data = resp.json()
    return data["bitcoin"]["eur"]


def main():
    price = get_btc_price_eur()
    print(f"Current Bitcoin price in EUR: {price}")
    # For testing the API manually run this in the main directory
    # python3 -m price.btc_price


if __name__ == "__main__":
    main()
