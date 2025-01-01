from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, Compusurf!"  # Let op die spasie voor hierdie lyn.

@app.route('/data', methods=['POST'])
def handle_data():
    data = request.json
    print(data)  # Log die inkomende data
    return {"status": "success", "data": data}, 200

from flask_cors import CORS
CORS(app)

from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///compusurf.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

db.create_all()
