import os
from dotenv import load_dotenv

# Load .env variables (for local dev, ignored in K8s)
load_dotenv()

# SMTP configuration
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SMTP_USERNAME = os.getenv("SMTP_USERNAME")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
NOTIFICATION_EMAIL_TO = os.getenv("NOTIFICATION_EMAIL_TO")

# Other config
BTC_PRICE_API = "https://api.coingecko.com/api/v3/simple/price"
HTTP_TIMEOUT = 5

# In K8s, SERVICE_A_URL env var will point to the service DNS name
# Locally, falls back to localhost
SERVICE_A_BASE = os.getenv("SERVICE_A_URL", "http://127.0.0.1:5000/api")
