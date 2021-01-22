from flask import Flask, request
import pymysql.cursors
from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_DATABASE = os.getenv('DATABASE')

app = Flask(__name__)


conn = pymysql.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_DATABASE
)


@app.route('/login', methods=['POST'])
def login():
    try:
        if not request.json:
            return {
                'error': 'Invalid input'
            }

        username = request.json['username']
        password = request.json['password']

        with conn.cursor() as cur:
            sql = 'select id from users where ' \
                  'username = \'' + username + '\' ' \
                  'and password = \'' + password + '\''            

            cur.execute(sql)

            if cur.rowcount == 0:
                return {
                    'error': 'Invalid username or password'
                }

            return {
                'success': True
            }

    except KeyError:
        return {
                'error': 'Invalid input'
            }


if __name__ == "__main__":
    app.run()    
