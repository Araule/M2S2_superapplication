from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
# from pydantic import BaseModel
# from typing import Literal, Optional
# from uuid import uuid4
# from fastapi.encoders import jsonable_encoder

# import json
# import os

# Initialisation de l'application
app = FastAPI()

#Cette ligne active le moteur de template Jinja et indique que les templates HTML seront stockés dans le dossier "templates"
templates = Jinja2Templates(directory="templates")

# Cette ligne indique que les fichiers statiques (images, css) seront placés dans le dossier nommé "static"
app.mount("/static", StaticFiles(directory="static"), name="static")


# Modification de la route pour renvoyer du HTML
@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/tutorial", response_class=HTMLResponse)
async def tutorial(request: Request):
    return templates.TemplateResponse("tutorial.html", {"request":request})
