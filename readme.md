# Casting Agency API 
 

### Installing Dependencies for the Backend

1. **Python 3.7** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)


2. **Virtual Enviornment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)


3. **PIP Dependencies** - Once you have your virtual environment setup and running, install dependencies by running:
```bash
pip install -r requirements.txt
```
This will install all of the required packages we selected within the `requirements.txt` file.


4. **Key Dependencies**
 - [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

 - [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

 - [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 
  This will install all of the required packages we selected within the `requirements.txt` file.



## Running the server

From within the directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
. ./setup.sh
flask run
```

#### Flask run tests the token headers set for the enviroment. If they have expired, you need to login using the crededntials below and replace them in setup.sh and run setup.sh again

setup.sh has all the environment variables needed for the project. The app may fail if they are not set properly. If that happens just copy paste lines from setup.sh on you CLI.

# Project deployed at

https://radiant-sands-87798.herokuapp.com/


###### To test live APIs the only way right now to do this is curl requests. Add Auth token headers from logins below to test.

### AUTH0

The complete documentation for the authorization code flow can be found in [Auth0's Documentation](https://auth0.com/docs/api/authentication#authorize-application).

It may help to fill in the url in the textbox below before copying it into the browser:
```
https://{{YOUR_DOMAIN}}/authorize?audience={{API_IDENTIFIER}}&response_type=token&client_id={{YOUR_CLIENT_ID}}&redirect_uri={{YOUR_CALLBACK_URI}}
```
For this project
```
https://dev-w0m27pwl.us.auth0.com/authorize?audience=movies&response_type=token&client_id=FuDZfXiRt6E3MH150m2NUJUs28PX4gU6&redirect_uri=https://radiant-sands-87798.herokuapp.com/callback

```

casting Assistant token assistant@test.com Password12345

```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJoZDZRcHVGTTh1RjZTcWg3WmNHbiJ9.eyJpc3MiOiJodHRwczovL2Rldi13MG0yN3B3bC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjE3NWJkYjkwMmIzZGQwMDcxY2Q5YzM4IiwiYXVkIjpbIm1vdmllcyIsImh0dHBzOi8vZGV2LXcwbTI3cHdsLnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2MzUyNzk5OTIsImV4cCI6MTYzNTM2NjM5MiwiYXpwIjoiRnVEWmZYaVJ0NkUzTUgxNTBtMk5VSlVzMjhQWDRnVTYiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsidmlldzphY3RvcnMiLCJ2aWV3Om1vdmllcyJdfQ.BWgj3uKWaIzgSTSwzrpKTKWqx8usvEIz-2gPZQufVbl3nW_cHYzCvXAsOGQVjVCBwIoGqUF7akLYGLdz5pnSYzmg0YENsETDm0I-TwjMdl8NKGCOloP0gCcqtRf4iZmxGMW8g-a7Sc3ZmpI88EB3iXtKSgIOU2MBBUYXfCrTE-JuikcT20SBKbOckQv_ro7DBO5RlNRcB7G7visXx_lY9-Uz0nqMyEt88Bm76xfFN4WSsd_seKXqoSJNLtqf4kJOxPr4SuXHm8oLHoSmihFtgDaksPa1KJB7OGVScJ4F_-O8akUffLI7jleg348UyFX9iPQngwurBYrvG64lgQUlfw

```

Casting director token director@test.com Password12345

```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJoZDZRcHVGTTh1RjZTcWg3WmNHbiJ9.eyJpc3MiOiJodHRwczovL2Rldi13MG0yN3B3bC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjE3NWJlYmY3MmVmYTgwMDY5ZDI2YTJmIiwiYXVkIjpbIm1vdmllcyIsImh0dHBzOi8vZGV2LXcwbTI3cHdsLnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2MzUyODAwODksImV4cCI6MTYzNTM2NjQ4OSwiYXpwIjoiRnVEWmZYaVJ0NkUzTUgxNTBtMk5VSlVzMjhQWDRnVTYiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiYWRkOmFjdG9ycyIsImRlbGV0ZTphY3RvcnMiLCJlZGl0OmFjdG9ycyIsImVkaXQ6bW92aWVzIiwidmlldzphY3RvcnMiLCJ2aWV3Om1vdmllcyJdfQ.XD8TMfUvISSpQQgmw0ZUlSXJKRXu-XpZSXfA5J0vgZFkE-3qjeUpFR4-qwn8gdYqwkQacC2nZ22sfb0u88sdy2XmALFRWIzvOHOWhVjlKDMffr9VDQZQSlo1R-FLolVwkKLWCnsINB7KkpvWptv0-e2wEQd-c8HmM5B84__f0Z6s2zu666mQV_WT5aPk5KcRxEJEmAn9GYrCYBPqXfHYAoLlnPgAvfshtcm_qiFkG4nIk5WjVujUNnfd0TlUeEb1QHe7ijF5UX9V1OWcPWpmBnLj66dwNU3sscuqd2-Wr1vU7F9wK9bYVN1KZlIPdwBXcEWyIJKEd5JJuoX4R-Cx7Q

```

Executive Producer producer@test.com Password12345

```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJoZDZRcHVGTTh1RjZTcWg3WmNHbiJ9.eyJpc3MiOiJodHRwczovL2Rldi13MG0yN3B3bC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjE3NWJlMDI3MmVmYTgwMDY5ZDI2YTAxIiwiYXVkIjpbIm1vdmllcyIsImh0dHBzOi8vZGV2LXcwbTI3cHdsLnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2MzUyNzk0NzIsImV4cCI6MTYzNTM2NTg3MiwiYXpwIjoiRnVEWmZYaVJ0NkUzTUgxNTBtMk5VSlVzMjhQWDRnVTYiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiYWRkOmFjdG9ycyIsImFkZDptb3ZpZXMiLCJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImVkaXQ6YWN0b3JzIiwiZWRpdDptb3ZpZXMiLCJ2aWV3OmFjdG9ycyIsInZpZXc6bW92aWVzIl19.K-3pZUeegq_T173OB8PWL2xkGQ_JQrFwvRJ1FYfdl5zqpe85_rAeY3uyALcq0D4zC58zO-OtwwZnntsEM1URySVnWSTKNvRIPImPCKLRLMT1yk0k9AQQsy2GDD2_NukG03KmuSbow71aWvb9-CWbn7lUH2-EXOx4tB3irzGv9YeUb33__PFXJ4-QKboNQyUAANV1GeOEwPUIIGvTZn-V1KZ69WEoyvHiIunx1tbPtMJtLoe9yojFDW8iUATN36_JQeYhYwOqHU4YFsc-LoYgePn4SXov8GKbprXk-9TKaSXFHw_-jY-UmPTjkE4iKu2MBOV1cI4sozc_gJCbpSSRjg
```


## Testing
To run the tests, run 
```
dropdb casting_test
createdb casting_test
psql casting_test < casting.psql
python test_app.py
```

To run tests using Heroku endpoints, run in postman

```
casting.postman_collection.json
```




## API Reference

### Endpoints

GET '/actors'
POST '/actors'
PATCH '/actors/id'
DELETE '/actors/id'
GET '/movies'
POST '/movies'
PATCH '/movies/id'
DELETE '/movies/id'





#### GET '/movies?page=page number'
- Fetches a paginated dictionary of movies :
    - *Request parameters (optional): page number
    - *Returns: a list of movies paginated 10 movies per page,and total number of movies
    - Role Authorized: Assistant, Director, Producer
- Example: ```curl -H "Authorization: Bearer <Token>" http://127.0.0.1:5000/movies```
```
{
  "movies": [
    {
      "genre": "Animation/Family",
      "id": 4,
      "release_date": "2021-09-21",
      "title": "Ron's Gone Wrong"
    },
    {
      "genre": "Action/Sci-fi",
      "id": 1,
      "release_date": "2021-10-05",
      "title": "Venom: Let There Be Carnage"
    },
    {
      "genre": "Action/Adventure",
      "id": 2,
      "release_date": "2021-10-05",
      "title": "No Time To Die"
    },
    {
      "genre": "Horror/Thriller",
      "id": 3,
      "release_date": "2021-09-21",
      "title": "Halloween Kills"
    }
  ],
  "success": true,
  "total_movies": 4
}
```
#### GET '/actors?page=page number'
- Fetches a paginated dictionary of actor :
    - *Request parameters (optional): page number
    - *Returns: a list of actors paginated 10 actors per page,and total number of actors
    - Role Authorized: Assistant, Director, Producer
- Example: ```curl -H "Authorization: Bearer <Token>" http://127.0.0.1:5000/actors```
```
{
  "actors": [
    {
      "age": 30,
      "gender": "M",
      "id": 1,
      "name": "zaid"
    },
    {
      "age": 30,
      "gender": "M",
      "id": 2,
      "name": "ahmad"
    }
  ],
  "success": true,
  "total_actors": 2
}
```

#### POST '/movies'
- create  new movie and add it to the database :
    - *Request body:* JSON { 'title': 'new title', 'release_date': '2021-02-21','genre': "Action"}
    - *Returns : id of the created movie,and total number of movies
    - Role Authorized: Producer
- Example: ```curl -X POST -H "Content-Type: application/json" -H  "Authorization: Bearer <Token> " -d '{"title": "Call Me by Your Name", "release_date": "2017-10-20","genre": "Action"}' http://127.0.0.1:5000/movies```
```
{
  "created": 2,
  "success": true,
  "total_movies": 2
}
```

#### POST '/actors'
- create  new actor and add it to the database:
    - *Request body:* JSON {"name": "new name", "age": 30, "gender": "male", }
    - *Returns : id of the created actor,and total number of actors
    - Role Authorized: Director, Producer
- Example: ```curl -X POST -H "Content-Type: application/json" -H  "Authorization: Bearer <Token> " -d '{"name": "zaid","age": 30,"gender": "male"}' http://127.0.0.1:5000/actors```

```
{
  "created": 2,
  "success": true,
  "total_actors": 2
}
```

#### PATCH '/movies/<int:id>'
- Update some information of a movie:
    - *Request body:* JSON of the information that want to update { (optional)'title': 'new title',(optional) 'release_date': '2021-02-21',(optional) 'genre': "Action"}
    - *Returns : the updated movie
    - Roles authorized : Director, Producer.
- Example: ```curl http://127.0.0.1:5000/movies/1 -X PATCH -H "Content-Type: application/json" -H "Authorization: Bearer <token>" -d '{ "title": "", "release_date": "2020-11-01" }''```
```
{
  "movie": {
    "genre": "Action",
    "id": 1,
    "release_date": "2020-11-01",
    "title": ""
  },
  "success": true
}
```

#### PATCH '/actors/<int:id>'
- Update some information of an actor :
    - *Request body:* JSON of the information that want to update {(optional)"name": "new name", (optional)"age": 30,(optional) "gender": "male", }
    - *Returns : the created actor
    - Roles authorized : Director, Producer.
- Example: ```curl http://127.0.0.1:5000/actors/1 -X PATCH -H "Content-Type: application/json" -H "Authorization: Bearer <token>" -d '{"name": "", "age": 88 }'```
```
{
  "actor": {
    "age": 88,
    "gender": "male",
    "id": 1,
    "name": ""
  },
  "success": true
}
```

#### DELETE '/movis/<int:id>'
- Delete movie by id from the database:
    - *Request arguments: movie id  
    - *Returns : id of the deleted movie 
    - Roles authorized :  Producer.
- Example: ```curl -H "Authorization: Bearer <TOKEN>" -X DELETE http://127.0.0.1:5000/movies/2```
```
{
  "deleted": 2,
  "success": true
}
```

#### DELETE '/actors/<int:id>'
- Delete actor by id from the database:
    - *Request arguments: actor id  
    - *Returns : id of the deleted actor 
    - Roles authorized :  Director,  Producer.
- Example: ```curl -H "Authorization: Bearer <TOKEN>" -X DELETE http://127.0.0.1:5000/actors/1```
```
{
  "deleted": 1,
  "success": true
}
```

### Error Handling
Errors are returned in the following json format:
```
{
    'success': False,
    'error': 404,
    'message': 'Resource not found. Input out of range.'
}
```
The API returns 4 types of errors:
- 400: bad request
- 404: not found
- 422: unprocessable
- AuthError: which mainly results in (unauthorized)

# alibabpythonproject
# python-project
# python-project
