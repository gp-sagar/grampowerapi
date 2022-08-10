from flask import Flask, jsonify
# from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL, MySQLdb

app = Flask(__name__)

app.secret_key = 'super-secret-key'

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'grampower'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)


@app.route('/')
def index():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT * FROM grampower_data")
    rv = cur.fetchall()

    response = [
        {
            "bg_image": item["bg_img"],
            "button": item["btn"],
            "description": item["dess"],
            "imgae": item["img"],
            "id": item["series_no"],
            "title": item["title"],
        } for item in rv
    ]
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
