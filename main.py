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
from scripts import dico
import random

#=== les fonctions extérieures
def util_get_infos(sentence: str):
    """ permet d'obtenir un dictionnaire contenant les informations demandées

    Args:
        sentence (str): la phrase rentrée par l'utilisateur, peut-être également
            un mot ou un caractère
    """
    return dico.main(sentence)

#=== initialisation de l'application
app = FastAPI() # initialisation de l'app
templates = Jinja2Templates(directory="templates") # active le moteur de template Jinja et indique l'emplacement des templates HTML
app.mount("/static", StaticFiles(directory="static"), name="static") # indique l'emplacement des fichiers statiques (images, css)

#=== les root app.get affichent les templates
@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/about")
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

#=== les root app.post et app.get transmettent/gèrent les données
# 'app.get' nous sert à vider le cache quand l'utilisateur clique sur Dictionnaire DWJ ou Home
@app.get("/", response_class=HTMLResponse) 
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/", response_class=HTMLResponse)
async def root(request: Request):
    form_data = await request.form() # récupère les valeurs du formulaire
    tokens = form_data.get('tokens') # valeur du champ name="tokens" dans le formulaire
    infos, cntype = util_get_infos(tokens) # appel à la fonction extérieure pour gérer l'ajout dans la BDD
    print(infos) # affiche sur le terminal pour le debuggage
    print("TYPE/", cntype)
    return templates.TemplateResponse("index.html", {"request": request, "results": infos, "cntype": cntype})
