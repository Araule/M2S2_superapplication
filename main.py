#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" l'application peut être lancé de cette façon:
        $ uvicorn main:app --reload
"""

#=== les librairies importées
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

#=== initialisation de l'application
app = FastAPI() # initialisation de l'app
templates = Jinja2Templates(directory="templates") # active le moteur de template Jinja et indique l'emplacement des templates HTML
app.mount("/static", StaticFiles(directory="static"), name="static") # indique l'emplacement des fichiers statiques (images, css)

#=== les root app.get affichent les templates
@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/tutorial")
async def tutorial(request: Request):
    return templates.TemplateResponse("tutorial.html", {"request": request})

@app.get("/about")
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})
