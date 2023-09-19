#import Flask
from flask import Flask

#instance de l'objet Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World'