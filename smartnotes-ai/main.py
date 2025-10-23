from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {{"status": "ok", "service": "smartnotes-ai"}}

@app.get("/")
def root():
    return {{"message": "Welcome to smartnotes-ai!"}}
