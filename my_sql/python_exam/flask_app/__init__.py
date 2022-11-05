from flask import Flask 
import re

app=Flask(__name__)
app.secret_key = "this_is_secret"

DATABASE = "sasquatch_sightings"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 