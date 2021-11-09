from fastapi import FastAPI

app = FastAPI()


@app.post(path="/analyse-string")
async def analyse_string():
    pass
