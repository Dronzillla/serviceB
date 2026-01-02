# Bitcoin Price Alert Worker

This service is a worker that periodically checks the current Bitcoin price and compares it against active alerts retrieved from **Service A**. If the price falls below a user's defined threshold, it sends an email notification and deactivates the alert in Service A.

This project is designed to demonstrate:
- **Kubernetes (Minikube)** deployment.
- **Service-to-Service Communication** (Service B talking to Service A).
- **Environment Variable Configuration** in a containerized environment.

## Features

- Fetches current Bitcoin price in EUR via CoinGecko API.
- Retrieves active alerts from an external service (Service A).
- Triggers email notifications via SMTP (e.g., Gmail).
- Deactivates triggered alerts to prevent duplicate notifications.

## Prerequisites

- Python 3.12+
- Docker (optional, for containerization)
- Kubernetes/Minikube (optional, for orchestration testing)

## Configuration

The service is configured using environment variables. You can set these in a `.env` file for local development or in Kubernetes manifests.

| Variable | Description | Default |
|----------|-------------|---------|
| `SMTP_SERVER` | SMTP server address | `smtp.gmail.com` |
| `SMTP_PORT` | SMTP server port | `587` |
| `SMTP_USERNAME` | SMTP username (email) | **Required** |
| `SMTP_PASSWORD` | SMTP password (or app password) | **Required** |
| `SERVICE_A_URL` | Base URL for Service A API | `http://127.0.0.1:5000/api` |

## Local Development

1. **Clone the repository** (if you haven't already).

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up configuration**:
   Create a `.env` file in the root directory:
   ```ini
   SMTP_USERNAME=your-email@gmail.com
   SMTP_PASSWORD=your-app-password
   # Ensure Service A is running locally on port 5000
   SERVICE_A_URL=http://127.0.0.1:5000/api
   ```

4. **Run the worker**:
   ```bash
   python main.py
   ```

## Docker Usage

1. **Build the image**:
   ```bash
   docker build -t bitcoin-alert-worker .
   ```

2. **Run the container**:
   ```bash
   docker run --env-file .env bitcoin-alert-worker
   ```

## Kubernetes (Minikube) & Service Communication

This service is intended to run alongside **Service A** in a Kubernetes cluster.

### Service Discovery
When running in Kubernetes, this worker needs to communicate with Service A using its internal DNS name.

Example `Deployment` configuration snippet for this worker:

```yaml
env:
  - name: SERVICE_A_URL
    value: "http://service-a.default.svc.cluster.local:5000/api"
  - name: SMTP_USERNAME
    valueFrom:
      secretKeyRef:
        name: smtp-secrets
        key: username
  - name: SMTP_PASSWORD
    valueFrom:
      secretKeyRef:
        name: smtp-secrets
        key: password
```

*Note: Replace `service-a` with the actual Service name of your Service A deployment.*

### Testing with Minikube

1. Start Minikube: `minikube start`
2. Build images in Minikube's Docker daemon:
   ```bash
   eval $(minikube -p minikube docker-env)
   docker build -t bitcoin-alert-worker .
   ```
3. Deploy Service A and this worker (Service B) using Kubernetes manifests.
4. Verify logs to see the communication:
   ```bash
   kubectl logs -l app=bitcoin-alert-worker
   ```
