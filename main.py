from fastapi import FastAPI

app = FastAPI()

@app.get("/test")
async def root():
    return "Funcionando perfectamente!"

@app.get("/url")
async def url():
    return { "GitHub Profile":"https://github.com/Agusdigiam" }

@app.post("/create")
async def create()