import requests
from config import SERVICE_A_BASE, HTTP_TIMEOUT


def get_active_alerts():
    url = f"{SERVICE_A_BASE}/alerts?active=true"
    resp = requests.get(url, timeout=HTTP_TIMEOUT)
    resp.raise_for_status()
    return resp.json()["data"]["alerts"]


def deactivate_alert(alert_id: int):
    url = f"{SERVICE_A_BASE}/alerts/{alert_id}"
    resp = requests.patch(url, json={"active": False}, timeout=HTTP_TIMEOUT)
    resp.raise_for_status()
