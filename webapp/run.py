from web.views import create_app

app = create_app()

from prometheus_client import start_http_server, Counter, Gauge
import threading

REQUEST_COUNT = Counter('flask_requests_total', 'Total requests')
CPU_USAGE = Gauge('system_cpu_usage', 'CPU usage %')

def monitor_cpu():
    import psutil
    while True:
        CPU_USAGE.set(psutil.cpu_percent(interval=1))

threading.Thread(target=monitor_cpu, daemon=True).start()
start_http_server(8000)
