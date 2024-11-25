#initialise and setup fastapi
#also add the routes from the router.py file
#also initiate a mongodb connection on startup and close the same when the server shuts down
#also add cors and clear all the logs

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

#add cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


#add the routes
from .router import *


