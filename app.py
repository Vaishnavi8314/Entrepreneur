from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from app import create, read, update, delete
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new1.db'
db = SQLAlchemy(app)
meta = db.MetaData()
entrepreneur = db.Table(
    'entrepreneur', meta,
    db.Column('Student_USN', db.String, primary_key=True),
    db.Column('Company_name', db.String),
    db.Column('Company_website', db.String),
    db.Column('Company_email', db.String)
)
meta.create_all(db.engine)

@app.route('/create', methods=['POST'])
def add():
    result = create(request.get_json())
    return "Inserted successfully"

@app.route('/read', methods=['GET'])
def view():
    result = read()
    return result

@app.route('/update', methods=['PUT'])
def change():
    result = update(request.get_json())
    return "Updated Successfully"

@app.route('/delete', methods=['DELETE'])
def deleting():
    result = delete(request.get_json())
    return "Deleted successfully"

if __name__ == '__main__':
    app.run(debug=True, port=5000)
