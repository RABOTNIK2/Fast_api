from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse, PlainTextResponse, JSONResponse
from fastapi import status
from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import date
from enum import Enum

import mimetypes

app = FastAPI(
    title='big cock'
)

fake_cocks = [
    {'id': 1, 'size': "cyka_blyat", 'skin_color':'black', 'race':'nigga'},
    {'id': 2, 'size': 256, 'skin_color':'white', 'race':'europian'},
    {'id': 3, 'size': 256, 'skin_color':'green', 'race':'chinesse', 'balls':[
        {'id':1, 'created_date': '1987-01-16', 'quality_of_semen': 'good'}
    ]}
]

@app.get('/cock_color/{color}')
def dsiplay_cock_by_color(color: str):
    return [cock.get('size') for cock in fake_cocks if cock.get('skin_color')==color]

class SemenQuality(Enum):
    bad = 'bad'
    good = 'good'
    mythical = 'mythical'
    legendary = 'legendary'

class Balls(BaseModel):
    id:int
    created_date:date
    quality_of_semen: SemenQuality

class Cock(BaseModel):
    id:int
    size:int
    skin_color:str
    race:str
    balls:Optional[List[Balls]] = []

@app.get('/cock_list/cock_user/', response_model=List[Cock])
def display_personal_cock(id:int):
    return [user for user in fake_cocks if user.get('id') == id ]

@app.post('/cock_change/{cock_id}')
def change_cock(cock_id: int, new_size:int, new_color:str):
    current_cock = list(filter(lambda cock: cock.get('id')==cock_id, fake_cocks))[0]
    if (new_size or new_color) is None:
        return JSONResponse(content={'message':'вы ничего не вписали'}, status_code=status.HTTP_400_BAD_REQUEST)
    current_cock['size'] = new_size
    current_cock['color'] = new_color
    return JSONResponse(content={'message':f'{current_cock}'}, status_code=status.HTTP_200_OK)

class Cocks(BaseModel):
    id: int
    size: int = Field(ge=0)
    skin_color:str
    race:str

@app.post('/cock_add')
def add_cock(cocks: List[Cocks]):
    fake_cocks.extend(cocks)
    return {'data':f'{fake_cocks}'}

# @app.get("/IAMBASIGN")
# def root():
#     return FileResponse("jopa/index.html", 
#                         filename="i_am_batukhan.html", 
#                         media_type="application/octet-stream")
    
# @app.get('/YOUGIMMEITALL', response_class=FileResponse)
# def toor():
#     return 'jopa/index.html'

# @app.get('/ambouttofukinnut')
# def roto(name:str, age:int):
#     data = f'<h1>Ваше имя: {name}, ваш возраст {age}, вы гомосек</h1>'
#     return HTMLResponse(content=data)