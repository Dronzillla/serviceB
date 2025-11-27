from price.btc_price import get_btc_price_eur
from alerts.client import get_active_alerts, deactivate_alert
from notifications.notify import send_notification


def run():
    price = get_btc_price_eur()
    print(f"Fetched BTC price: {price}")

    alerts = get_active_alerts()
    print(f"Found {len(alerts)} active alerts.")

    for alert in alerts:
        if price <= alert["threshold"]:
            print(f"Triggering alert {alert['id']}")
            send_notification(alert["email"], alert["threshold"], price)
            deactivate_alert(alert["id"])


if __name__ == "__main__":
    run()
