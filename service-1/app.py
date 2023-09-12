from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app, path="/metrics")

metrics.info("app_info", "service1", version="1.0.0")

@metrics.counter(
    "invocation_by_method",
    "Number of invocations by HTTP method",
)

@app.route('/')
def hello():
  return 'Hello World!'

if __name__ == '__main__':
  app.run(host="0.0.0.0", port=5001, debug=False)