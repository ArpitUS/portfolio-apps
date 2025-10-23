FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN if exist requirements.txt pip install -r requirements.txt || echo "No Python dependencies"
CMD ["python3", "-m", "http.server", "8080"]
