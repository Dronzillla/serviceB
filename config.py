import os

# Address inside Kubernetes cluster
SERVICE_A_BASE = os.getenv("SERVICE_A_BASE", "http://service-a:5000/api")

# External BTC price API
BTC_PRICE_API = "https://api.coingecko.com/api/v3/simple/price"

# Default timeout for HTTP calls
HTTP_TIMEOUT = 10
