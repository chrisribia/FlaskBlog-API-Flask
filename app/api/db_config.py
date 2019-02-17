import os

import psycopg2 as p
import psycopg2.extras
from werkzeug.security import generate_password_hash

DATABASE_URL = os.getenv('DATABASE_URL')
DATABASE_URL_TEST = os.getenv('DATABASE_URL_TEST')

def connection(url):
    conn = p.connect(url)
    return conn


def destroy_tables():
    conn = connection(DATABASE_URL)
    cursor = conn.cursor()
    
    users = "DROP TABLE  users "
    blogs = "DROP TABLE  blogs "
    comments = "DROP TABLE comments "
    queries = [blogs, users, comments]
    try:
       for query in queries:
            cursor.execute(query)
            con.commit()
            print('Destroying test tables...Done ')
    except :
        print("Failed to Destroy tables")

def create_tables():
    '''A database cursor is an object that points to a
    place in the database where we want to create, read,
    update, or delete data.'''
    conn = connection(DATABASE_URL)
    cursor = conn.cursor()
    queries = tables()

    try:
        for query in queries:
            cursor.execute(query)
        conn.commit()
        print('Creating Tables.....Done')
    except:
        print("Failed to Create tables")   

def tables():
    tbl1 = """CREATE TABLE IF NOT EXISTS blogs (
    blog_id serial PRIMARY KEY NOT NULL,
    user_id INT NOT NULL,
    title character varying(200) NOT NULL,
    description character varying(1000),
    date_created timestamp with time zone DEFAULT ('now'::text)::date NOT NULL
    )"""

    tbl2 = """create table IF NOT EXISTS users (
     user_id serial PRIMARY KEY NOT NULL,
     user_name character(50) NOT NULL,
     first_name character(50),
     last_name character(50),
     email varchar(50) NOT NULL,
     isAdmin boolean NOT NULL,  
     registered timestamp with time zone DEFAULT ('now'::text)::date NOT NULL, 
     password varchar(500) NOT NULL
     )"""


    tbl3 = """CREATE TABLE IF NOT EXISTS comments (
    comment_id serial PRIMARY KEY NOT NULL,
    blog_id INT NOT NULL,
    user_id INT NOT NULL,
    comment character varying(1000) NOT NULL,
    up_votes numeric DEFAULT 0,
    date_created timestamp with time zone DEFAULT ('now'::text)::date NOT NULL,
    user_preferred boolean DEFAULT false
    )"""

    queries = [tbl1, tbl2,tbl3]
    return queries
 
