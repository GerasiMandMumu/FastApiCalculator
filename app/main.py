from fastapi import FastAPI, Response, Body, Form
from fastapi.responses import JSONResponse, FileResponse
from fastapi.encoders import jsonable_encoder


def calculate(phrase):
    exec(f'result = ({phrase})')
    return result
   
app = FastAPI()

@app.get("/")
async def root():
    return FileResponse("index.html")
    #return {"message": "Hello, World!"}

@app.get("/eval/{phrase}")
async def eval(phrase: str):
    result = phrase
    print(result.split('+'))
    data = {'Результат = ': result}
    json_data = jsonable_encoder(data)
    return JSONResponse(content=json_data, media_type="text/plain", status_code=200)


@app.post("/eval")
async def eval(phrase: str = Form()):
    data = {'Результат = ': phrase}
    json_data = jsonable_encoder(data)
    return JSONResponse(content=json_data, media_type="text/plain", status_code=201)

