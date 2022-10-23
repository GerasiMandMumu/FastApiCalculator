from fastapi import FastAPI, Body, Query
from fastapi.responses import JSONResponse, FileResponse, PlainTextResponse
from fastapi.encoders import jsonable_encoder
import traceback

# вычисление выражения
def calculate(phrase: str) -> str:
    loc = {}
    exec(f'result = ({phrase})', globals(), loc)
    result = loc['result']
    return result
   
app = FastAPI()


# старт приложения
@app.get("/")
async def root():
    return FileResponse("app/index.html")


# GET-запрос
@app.get("/eval")
async def eval(phrase: str = Query(default=None, min_length=3)):
    
    # если выражение вычисляется, то выводится результат, иначе, сообщение об ошибке
    
    try:
        result = calculate(phrase)
        text_data = 'Результат = ' + str(result)
        response_status_code = 200
    except BaseException:
        response_status_code = 400
        text_data = traceback.format_exc()
    finally:
        return PlainTextResponse(content=text_data, status_code=response_status_code)

         
# POST-запрос
@app.post("/eval")
async def eval(data = Body(default=None)):
    
    # если выражение вычисляется, то выводится результат, иначе, сообщение об ошибке
    
    try:
        phrase = data["phrase"]
        result = calculate(phrase)
        data = {'result': result}
        json_data = jsonable_encoder(data)
        response_status_code = 201
    except BaseException:
        response_status_code = 400

        # получения описания ошибки
        tb = traceback.format_exc()
        data = {'result': tb}
        json_data = jsonable_encoder(data)
    finally:
        return JSONResponse(content=json_data, media_type="application/json", status_code=response_status_code)    

    
    
    

    

