from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {{"status": "ok", "service": "idea-validator-ai"}}

@app.get("/")
def root():
    return {{"message": "Welcome to idea-validator-ai!"}}
