from flask import Flask, render_template, request, json
from flaskext.mysql import MySQL
app = Flask(__name__)
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'multicloud'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


def sql_select(query):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    return rows

def sql_insert(query, var=None):
    conn = mysql.connect()
    cursor = conn.cursor()
    if var:
        cursor.execute(query, var)
    else:
        cursor.execute(query)
    conn.commit()
    conn.close()

def sql_delete(query,var=None):
    conn = mysql.connect()
    cursor = conn.cursor()
    if var:
        cursor.execute(query, var)
    else:
        cursor.execute(query)
    conn.commit()
    conn.close()

def sql_update(query, var=None):
    conn = mysql.connect()
    cursor = conn.cursor()
    if var:
        cursor.execute(query, var)
    else:
        cursor.execute(query)
    conn.commit()
    conn.close()