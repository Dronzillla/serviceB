import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

# SMTP configuration
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SMTP_USERNAME = os.getenv("SMTP_USERNAME")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
NOTIFICATION_EMAIL_TO = os.getenv("NOTIFICATION_EMAIL_TO")

# Other config
BTC_PRICE_API = "https://api.coingecko.com/api/v3/simple/price"
HTTP_TIMEOUT = 5
ALERT_THRESHOLD_EUR = 60000
SERVICE_A_BASE = "http://127.0.0.1:5000"
