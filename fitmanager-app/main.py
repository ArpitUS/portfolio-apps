from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {{"status": "ok", "service": "fitmanager-app"}}

@app.get("/")
def root():
    return {{"message": "Welcome to fitmanager-app!"}}
