from fastapi import FastAPI

app = FastAPI(title='AgroWatch API')

@app.get('/')
def read_root():
    return {'message': 'Welcome to AgroWatch API'}
