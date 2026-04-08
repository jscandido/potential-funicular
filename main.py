from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

#testeteste
#mais um testee
@app.get("/teste")
async def root():
    return {"teste": "teste!"}