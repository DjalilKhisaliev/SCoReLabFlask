from flask import Flask
from flask import request
import json
import os

app = Flask(__name__)

@app.route('/api/create', methods=['POST'])
def create():
    postdata = request.json
    name = postdata["name"]
    description = postdata["description"]
    try:
        note = open("{0}.txt".format(name), "w")
        note.write(description)
        return {"status":"OK"}
    except Exception as ex:
        return {"error": str(ex)}

@app.route('/api/read', methods=['GET'])
def read():
    name = request.args.get('name', default = None, type = str)
    if name == None:
        return {"error": "You need to set the name of note"}
    try:
        note = open("{0}.txt".format(name), "r")
        desc = note.read()
        return desc
    except Exception as ex:
        return {"error": str(ex)}
        
#yes, i know that the main different of update and create functions is the name)
@app.route('/api/update', methods=['POST'])
def update():
    postdata = request.json
    name = postdata["name"]
    description = postdata["description"]
    try:
        note = open("{0}.txt".format(name), "w")
        note.write(description)
        return {"status":"OK"}
    except Exception as ex:
        return {"error": str(ex)}
        
@app.route('/api/delete', methods=['POST', 'GET'])
def delete():
    name = request.args.get('name', default = None, type = str)
    if name == None:
        return {"error": "You need to set the name of note"}
    try:
        os.remove("name")
    except Exception as ex:
        return {"error": str(ex)}



if __name__ == '__main__':
    app.run(host= '0.0.0.0', port = 9999)