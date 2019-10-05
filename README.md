 [![Build Status](https://travis-ci.org/chrisribia/FlaskBlog.svg?branch=master)](https://travis-ci.org/chrisribia/FlaskBlog) [![Coverage Status](https://coveralls.io/repos/github/chrisribia/FlaskBlog/badge.svg)](https://coveralls.io/github/chrisribia/FlaskBlog)
### Tech/framework used  
python 3.6.7 and [Flask](http://flask.pocoo.org/docs/dev/)   
### PROJECT OVERVIEW  
 
## Installation and Deployment. 
### Getting Started 
 
#### Create a virtual environment and activate it 
> python3 - m venv env  
> source .env  
#### Install all the dependencies using the command
> pip install -r requirements.txt
## contents of `.env`   
```  
source venv/bin/activate  

export FLASK_ENV="development"   
export FLASK_CONFIG="development"  
export DATABASE_URL="dbname='your-database' host='localhost' port='5432' user='your-username' password='your-password'"   
export DATABASE_URL_TEST="dbname='your-test-database' host='localhost' port='5432' user='your-username' password='your-password'"   
export SECRET_KEY="secret-key-goes-here"
``` 
#### How to Run the App
 ```   
source .env
> flask run   
```

#### Test the application  
Tests are to be run with pytest or py.test on the root folder
Set FLASK_CONFIG to testing on your .env file before running tests   

`source .env
pytest --cov=app/` 
 ### Documentation   
 ### Hosting link
 [Heroku](https://wakali-stack.herokuapp.com/)
