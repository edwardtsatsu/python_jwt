from fastapi import FastAPI


app = FastAPI()

@app.get('/', tags=['test endpoint'])
def greet():
    return {
        "message": "Hello World"
    }
