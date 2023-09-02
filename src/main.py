from fastapi import FastAPI

app = FastAPI(
    title='project 1'
)

@app.get("/")
def get_info():
    return {
        "status": "success",
        "details": "Hello, Alex!"
    }