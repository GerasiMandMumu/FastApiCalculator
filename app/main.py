from fastapi import FastAPI, Response, Path, Body
from fastapi.responses import JSONResponse, FileResponse, PlainTextResponse
from fastapi.encoders import jsonable_encoder
import traceback

def calculate(phrase: str) -> str:
    loc = {}
    exec(f'result = ({phrase})', globals(), loc)
    result = loc['result']
    return result
   
app = FastAPI()

@app.get("/")
async def root():
    return FileResponse("app/index.html")

@app.get("/eval/{phrase}", status_code=200)
async def eval(response: Response, phrase: str = Path(default=None, min_length=3)):
    try:
        result = calculate(phrase)
        text_data = 'Результат = ' + str(result)
        response.status_code = 200
    except BaseException:
        response.status_code = 400
        text_data = traceback.format_exc()
    finally:
        return PlainTextResponse(content=text_data)
         
    
@app.post("/eval")
async def eval(data = Body(default=None)):
    try:
        phrase = data["phrase"]
        result = calculate(phrase)
        data = {'result': result}
        json_data = jsonable_encoder(data)
        response_status_code = 200
    except BaseException:
        response_status_code = 400
        tb = traceback.format_exc()
        data = {'result': tb}
        json_data = jsonable_encoder(data)
    finally:
        return JSONResponse(content=json_data, media_type="application/json", status_code=response_status_code)    

    
    
    

    

