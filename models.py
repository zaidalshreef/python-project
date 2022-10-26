import  os
from flask_migrate import Migrate
from sqlalchemy import Column, String, create_engine
from flask_sqlalchemy import SQLAlchemy
import json


db = SQLAlchemy()

DATABASE_URI = "postgresql://postgres:987654321@localhost:5432/academy"

def setup_db(app, database_path=DATABASE_URI):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)


def setup_migrations(app):
    migrate = Migrate(app, db)


def create_and_drop_all():
    #db.drop_all()
    db.create_all()


# MoviesAndActors = db.Table('MoviesAndActors',
#     db.Column('Movie_id', db.Integer, db.ForeignKey('actor.id')),
#     db.Column('Actor_id', db.Integer, db.ForeignKey('movie.id')),)

class Teacher(db.Model):
    __tablename__ = 'teacher'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    age = db.Column(db.Integer(), nullable=False)
    gender = db.Column(db.String(), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    


    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return{
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender
            }

    def __repr__(self):
        return f'Teacher: {self.id}, {self.name}'


class Course(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(), nullable=False)
    teachers = db.relationship("Teacher",backref='course', lazy=True)
   
    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return{
            "id": self.id,
            "title": self.title,
            }

    def __repr__(self):
        return f'Course:{self.id}, {self.title}'