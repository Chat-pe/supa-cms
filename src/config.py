#extract the following env variable from the .env file
# here are the variables
# MONGO_URI
# PORT
# HOST
# DEBUG
# TESTING
# SECRET_KEY

import os
# from dotenv import load_dotenv #don't use dotenv

# files = load_dotenv("/src/dev.env")
# print("this is the file",files)

MONGO_URI = os.getenv("MONGO_URI","mongodb+srv://cms:12345@cms.sr0xt.mongodb.net/?retryWrites=true&w=majority&appName=cms")
PORT = os.getenv("PORT")
HOST = os.getenv("HOST")
DEBUG = os.getenv("DEBUG")
TESTING = os.getenv("TESTING")
SECRET_KEY = os.getenv("SECRET_KEY","9ca16c5e6de97079820e923dceae690eea3fa0dc3ca1ac3dfdc70f7c4d84e0e089c2638dc0a43c5bf912d9231bd8478ee666a049a79555b8900b995abf4d33a5")
