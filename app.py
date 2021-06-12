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
    query = "SELECT * FROM notes"
    cursos.execute(query)
    result = cursos.fetchall()
    print('received ' + str(len(result)) + ' notes')
    jsonedResult = jsonify(result)
    return jsonedResult


@app.route('/getNote', methods=['GET'])
def get_note():
    connection.commit()
    cursos = connection.cursor(dictionary=True)
    args = request.args
    id = args.get('id')
    query = "SELECT * FROM notes WHERE id = " + id
    cursos.execute(query)
    result = cursos.fetchone()
    print('received ' + str(len(result)) + ' note')
    jsonedResult = jsonify(result)
    return jsonedResult


@app.route('/deleteNote', methods=['POST'])
def delete_note():
    cursor = connection.cursor()
    noteId = str(request.json['id'])
    query = "DELETE FROM notes WHERE id = " + noteId
    cursor.execute(query)
    connection.commit()
    cursor.close()
    return 'delete complete'


@app.route('/addNote', methods=['POST'])
def add_note():
    cursor = connection.cursor()
    title = request.json['title']
    description = request.json['description']
    query = "INSERT INTO notes(title, description) VALUES ('" + title + "','" + description + "');"
    cursor.execute(query)
    connection.commit()
    cursor.close()
    return 'add complete'


if __name__ == '__main__':
    app.run()
