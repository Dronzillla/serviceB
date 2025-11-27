import smtplib
from email.mime.text import MIMEText
from config import SMTP_SERVER, SMTP_PORT, SMTP_USERNAME, SMTP_PASSWORD


def send_email_notification(to_email, subject, message):
    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = SMTP_USERNAME
    msg["To"] = to_email

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
            smtp.starttls()
            smtp.login(SMTP_USERNAME, SMTP_PASSWORD)
            smtp.send_message(msg)

        print("Notification sent!")

    except Exception as e:
        print(f"Error sending notification: {e}")


def main():
    send_email_notification(
        to_email=SMTP_USERNAME,
        subject="Btc price",
        message="Testing SMTP set up manually",
    )
    # For testing the SMTP manually run this in the main directory
    # python3 -m notifications.notify


if __name__ == "__main__":
    main()
