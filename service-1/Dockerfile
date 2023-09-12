FROM python
RUN pip install flask prometheus_flask_exporter
COPY ./app.py /app.py
CMD ["python", "app.py"]
