from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {{"status": "ok", "service": "habitwise-ai"}}

@app.get("/")
def root():
    return {{"message": "Welcome to habitwise-ai!"}}
