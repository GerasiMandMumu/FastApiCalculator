from fastapi import FastAPI, Response, Body, Form
from fastapi.responses import JSONResponse, FileResponse
from fastapi.encoders import jsonable_encoder


def calculate(phrase):
    loc = {}
    exec(f'result = ({phrase})', globals(), loc)
    result = loc['result']
    return result
   
app = FastAPI()

@app.get("/")
async def root():
    return FileResponse("index.html")

@app.get("/eval/{phrase}")
async def eval(phrase: str):
    result = calculate(phrase)
    data = {'Результат = ': result}
    json_data = jsonable_encoder(data)
    return JSONResponse(content=json_data, media_type="text/plain", status_code=200)


@app.post("/eval")
async def eval(phrase: str = Form('test')):
    result = calculate(phrase)
    data = {'Результат = ': result}
    json_data = jsonable_encoder(data)
    return JSONResponse(content=json_data, media_type="text/plain", status_code=201)

