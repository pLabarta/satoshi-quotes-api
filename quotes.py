# Satoshi Nakamoto Random Quote Generator
# Data from nakamotoinstitute.org
# Developed by Ullathorpe Studios

import json
from random import choice
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return get_random_quote()

def get_random_quote():
    f = open('data/quotes.json')
    data = json.load(f)
    quote = choice(data)
    f.close()
    return quote
    
if __name__ == "__main__":
    app.run()
