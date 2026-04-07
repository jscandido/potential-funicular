from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

#testeteste
@app.get("/teste")
async def root():
    return {"hello": "world!"}