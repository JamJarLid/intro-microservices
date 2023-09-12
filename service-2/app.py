from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics
import requests

app = Flask(__name__)
metrics = PrometheusMetrics(app, path="/metrics")

metrics.info("app_info", "service1", version="1.0.0")

@metrics.counter(
    "invocation_by_method",
    "Number of invocations by HTTP method",
)

@app.route("/")
def hello_world():
    r = requests.get("http://service1:5001")
    return f"Hello from Service 2. Service 1 says: {r.text}!"

if __name__ == '__main__':
  app.run(host="0.0.0.0", port=5002, debug=False)