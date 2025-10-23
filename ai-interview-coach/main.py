from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {{"status": "ok", "service": "ai-interview-coach"}}

@app.get("/")
def root():
    return {{"message": "Welcome to ai-interview-coach!"}}
