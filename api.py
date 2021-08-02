from flask import Flask
from flask_cors import CORS
from flask_restful import Resource,Api
import requests
import 


app = Flask(__name__)
CORS(app)

@app.route('/',methods=['GET'])

def home():
    a = 'dYNamite'
    b = 'Mjamaa'
    sum = a +''+ b
    
    
   # r = requests.get('https://jsonplaceholder.typicode.com/todos/1')

    
    return 
if __name__ == '__main__':
    app.run(debug=True,host = '127.0.0.1',port=666)
