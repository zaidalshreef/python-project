import os
from models import setup_db, Teacher, Course, create_and_drop_all, setup_migrations
import datetime
from flask import Flask, request, abort, jsonify,session,redirect,render_template,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from urllib.parse import urlencode


movies_or_actors_Per_Page = 10


def pagination_movie_or_actor(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * movies_or_actors_Per_Page
    end = start + movies_or_actors_Per_Page

    movies_or_actors = [movie_or_actor.format() for movie_or_actor in selection]
    current_movies_or_actors = movies_or_actors[start:end]
    return current_movies_or_actors


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    setup_migrations(app)
    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             "Content-Type,Authorization,true")
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PUT,POST,PATCH,DELETE,OPTIONS')
        return response

##--------------------------------------------------------------------------------##

                                    # course #

##--------------------------------------------------------------------------------##

   # get course from database
    @app.route('/course')
    def view_course():
        
    
        course = Course.query.all()
        if course is None:
            abort(404)
            
        total_course = len(course)
        current_course = pagination_movie_or_actor(request, course)

        return jsonify({"success": True,
                        "course": current_course,
                        "total_course": total_course
                        })



 # add a new course 
    @app.route('/course', methods=['POST'])
    def add_course():

        data = request.get_json()
        print(data)
        
        if data is None:
            abort(400)

        # abort if the request body is invalid
        if ('title' not in data):
            abort(400)

        try:
            course =  Course()
            course.title=data.get('title')
            # add the new  to the database
            course.insert()
            # get the movies ordered by id
            courses = Course.query.order_by(Course.id).all()
            # total number of movies in the database after insert the new movie
            total_courses = len(courses)
            # paginate the movies
            return jsonify({
                "success": True,
                "created": course.id,
                "total_course": total_courses,
                "title":course.title
            })

        except:
            abort(422)
            
            
            
     #edit the course by id 
    @app.route('/course/<int:id>', methods=['PATCH'])
    def edit_course(id):
      
        data = request.get_json()
           
        if data is None:
                abort(400)
                
        course = Course.query.get(id)
            
        if course is None:
                abort(404)
      
        try:
           
                
            if 'title' in data:
                course.title = data.get('title')
            
                
            course.update()
            
            return jsonify({
                "success": True,
                "course": course.format()
            })
        except :
             abort(422)

        
        
        
        
    @app.route('/course/<int:id>', methods=['DELETE'])
    def delete_course(id):
        
        course = Course.query.get(id)
            
        if course is None:
                abort(404)
                
        
        try:
           
            course.delete()
            
            return jsonify({
                "success": True,
                "deleted": course.id
            })
        except :
          abort(422)
        
        
        
 ##--------------------------------------------------------------------------------##

                                    # teacher #

##--------------------------------------------------------------------------------##

        
        
    @app.route('/teacher')
    def view_teacher():
        
        
            teacher = Teacher.query.all()
            
            if teacher is None:
                abort(404)
                
            total_teacher = len(teacher)
            current_teacher = pagination_movie_or_actor(request, teacher)
                
            return jsonify({
                "success": True,
                "actors": current_teacher,
                "total_teacher": total_teacher,
            })
        
        
    @app.route('/teacher', methods=['POST'])
    def create_teacher():
        
        
        data = request.get_json()
        
        if data is None: 
            abort(400)
            
        if ('name' not in data or 'age' not in data or 'gender' not in data):
                abort(400)
        try:
            
                
            teacher = Teacher(name=data.get("name"),
                          age=data.get("age"),
                          gender=data.get("gender")
                          )
            
            teacher.insert()
            
            # get the actors ordered by id
            teacher = Teacher.query.order_by(Teacher.id).all()
            # total number of actors in the database after insert the new actor
            total_teacher = len(teacher)
            # paginate the actors
            return jsonify({
                "success": True,
                "created": teacher.id,
                "total_teacher": total_teacher,
            })
        except :
            abort(422)
            
            
    
    @app.route('/teacher/<int:id>', methods=['PATCH'])
    def edit_teacher(id):
        
        data = request.get_json()
            
            
        if data is None:
                abort(400)
                
        teacher = Teacher.query.get(id)
            
        if teacher is None:
                abort(404)
                
        
        try:
            
            if 'name' in data:
                teacher.name = data.get("name")
                
            if 'age' in data:
                teacher.age = data.get("age")
                
            if 'gender' in data:
                teacher.gender = data.get("gender")
                
            teacher.update()
            
            return jsonify({
                "success": True,
                "teacher": teacher.format()
            })
        except :
            abort(422)     
            
       
    @app.route('/teacher/<int:id>', methods=['DELETE'])
    def delete_actor(id):
        
        teacher = Teacher.query.get(id)
            
        if teacher is None:
            abort(404)
                
        try:
            
            teacher.delete()
            
            return jsonify({
                "success": True,
                "deleted": teacher.id
                })
        except:
            abort(422)   
            
    
           
 ##--------------------------------------------------------------------------------##

                                    # ERROR HANDLER #

##--------------------------------------------------------------------------------##

        
    
    
    
# handle 404 error in the application
    @app.errorhandler(404)
    def not_found(error):
     return jsonify({
      "success": False,
      'error': 404,
      "message" : "The server can not find the requested resource"
      }
    ),404
  
  #handle 422 error in the application 
    @app.errorhandler(422)
    def unprocessable_entity(error):
     return jsonify({
      "success": False,
      "error": 422,
      "message": "The request was well-formed but was unable to be followed due to semantic errors."
    }),422
     
     
 # handle 400 error in the application 
    @app.errorhandler(400)
    def bad_request(error):
     return jsonify({
      "success": False,
      "error": 400,
      "message": "The server could not understand the request due to invalid syntax."
    }),400        
    
            
    return app


app = create_app()

if __name__ == '__main__':
    app.run(port=8080, debug=True)
