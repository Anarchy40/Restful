from flask import Flask
from flask_cors import CORS
from flask_restful import Resource,Api
import requests
from flask import render_template


app = Flask(__name__)
CORS(app)

@app.route('/',methods=['GET'])

def home():
    a = 'dYNamite'
    b = 'Mjamaa'
    sum = a + ''+ b
    
    
    #r = requests.get('https://jsonplaceholder.typicode.com/todos/2')
    
    
    #return  r.json()
    return '<h1 id="sus">This isn atest </h1><br><script> document.getElementById("sus".innerHTML = "This is the test!!"</script>' + sum
if __name__ == '__main__':
    app.run(debug=True,host = '127.0.0.1',port=666)
