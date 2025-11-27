from price.btc_price import get_btc_price_eur
from alerts.client import get_active_alerts, deactivate_alert
from notifications.notify import send_email_notification


def run():
    price = get_btc_price_eur()
    print(f"Fetched BTC price: {price}")

    alerts = get_active_alerts()
    print(f"Found {len(alerts)} active alerts.")

    for alert in alerts:
        if price <= alert["threshold"]:
            print(f"Triggering alert {alert['id']}")

            subject = f"BTC Alert Triggered (Threshold: {alert['threshold']} EUR)"
            message = (
                f"Hello!\n\nYour Bitcoin alert has been triggered.\n"
                f"Threshold: {alert['threshold']} EUR\n"
                f"Current price: {price} EUR\n\n"
                f"This alert is now deactivated."
            )

            # Use the email from the alert
            send_email_notification(alert["email"], subject, message)
            deactivate_alert(alert["id"])


if __name__ == "__main__":
    run()
