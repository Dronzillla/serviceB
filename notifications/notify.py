from datetime import datetime, timezone


def send_notification(email: str, threshold: float, price: float):
    print(
        f"[{datetime.now(timezone.utc).isoformat()}] "
        f"NOTIFY → email={email}, price={price}, threshold={threshold}"
    )
