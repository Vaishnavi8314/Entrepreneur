from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///n2.db'
db = SQLAlchemy(app)
meta = db.MetaData()
entrepreneur = db.Table(
    'faculty', meta,
    db.Column('Faculty_Id', db.String, primary_key=True),
    db.Column('Faculty_Name', db.String),
    db.Column('Gender', db.String),
    db.Column('Program', db.String),
    db.Column('Employment_type',db.String),
    db.Column('Highest_degree',db.String),
    db.Column('University_Name',db.String),
    db.Column('Passed_out_year',db.String),
    db.Column('Joining_date',db.String),
    db.Column('Designation',db.String),
    db.Column('Department',db.String),
    db.Column('No_of_students_mentored',db.String)
)
meta.create_all(db.engine)
