# Python_Assignment3

This is Assignment 3 for advanced programming in python course, this program can build a web server with login function, after login successfully will return a token to access protected page

## Installation

Make sure that you have installed pyjwt, flask and sqlalchemy libraries also postgreSQL

```
pip install pyjwt

pip install Flask

pip install Flask-SQLAlchemy

```

## Usage

Dowanload file and open Assignment3.py and make some changes
```
# connect to your database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://yourUsername:yourPassword@localhost/yourDBName'
```
## Example

After launch Assignment3.py you will have a link in terminal

```
http://127.0.0.1:5000/                              -- default page
http://127.0.0.1:5000/login                         -- login page
http://127.0.0.1:5000/protected                     -- default protected page
http://127.0.0.1:5000/protected?token='tokenValue'  -- protected page
```
