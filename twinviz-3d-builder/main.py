from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {{"status": "ok", "service": "twinviz-3d-builder"}}

@app.get("/")
def root():
    return {{"message": "Welcome to twinviz-3d-builder!"}}
