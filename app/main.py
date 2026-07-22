from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():

    return {

        "message": "AI Research Paper Analyzer Running"

    }