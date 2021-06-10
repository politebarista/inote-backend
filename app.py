from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

connection = mysql.connector.connect(host="localhost",
                             user="root",
                             password="root",
                             database="inote",
                             )


@app.route('/')
def index():
    return 'welcome)'


@app.route('/getNotes', methods=['GET'])
def get_notes():
    connection.commit()
    cursos = connection.cursor(dictionary=True)
    query = "select * from notes"
    cursos.execute(query)
    result = cursos.fetchall()
    print('received ' + str(len(result)) + ' notes')
    jsonedResult = jsonify(result)
    return jsonedResult


@app.route('/deleteNote', methods=['POST'])
def delete_note():
    cursor = connection.cursor()
    noteId = request.json['id']
    query = "DELETE FROM notes WHERE id = " + toString()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    print('delete testing')
    return 'delete complete'


@app.route('/addNote', methods=['GET'])
def add_note():
    cursor = connection.cursor()
    args = request.args
    title = args.get('title')
    description = args.get('description')
    query = "INSERT INTO notes(title, description) VALUES ('" + title + "','" + description + "');"
    cursor.execute(query)
    connection.commit()
    cursor.close()
    return 'add complete'


if __name__ == '__main__':
    app.run()
