from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {{"status": "ok", "service": "freelance-finance-tracker"}}

@app.get("/")
def root():
    return {{"message": "Welcome to freelance-finance-tracker!"}}
