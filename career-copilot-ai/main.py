from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {{"status": "ok", "service": "career-copilot-ai"}}

@app.get("/")
def root():
    return {{"message": "Welcome to career-copilot-ai!"}}
