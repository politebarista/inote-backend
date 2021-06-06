from flask import Flask, request, jsonify
import pymysql

app = Flask(__name__)

connection = pymysql.connect(host="localhost",
                             user="root",
                             password="root",
                             database="inote",
                             cursorclass=pymysql.cursors.DictCursor,
                             )


@app.route('/')
def index():
    return 'welcome)'


@app.route('/getNotes', methods=['GET'])
def get_notes():
    cursos = connection.cursor()
    query = "select * from notes"
    cursos.execute(query)
    result = cursos.fetchall()
    print('received ' + str(len(result)) + ' notes')
    jsonedResult = jsonify(result)

    return jsonedResult


if __name__ == '__main__':
    app.run()
