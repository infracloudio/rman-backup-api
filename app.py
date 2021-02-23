from flask import Flask,request,jsonify
import os
import subprocess

app = Flask(__name__)

@app.route("/healthcheck")
def ready():
    return "Service is ready!"

@app.route("/rman", methods=['POST'])
def rmanCommand():
    if not request.json or not 'connect_string' in request.json:
        abort(400)
    connect_string = request.json['connect_string']
    command = request.json['command'].lower()
    if command in ['list','backupcontrolfile','fullbackup','restore','dropdb']:
        result = subprocess.run(["bash","./rman.sh",connect_string, command] )
    else:
        return "invalid command"
    print("result=", result)
    return jsonify({'result': 200}), 200

@app.route("/rman/restore", methods=['POST'])
def rmanRestore():
    if not request.json or not 'connect_string' in request.json:
        abort(400)
    connect_string = request.json['connect_string']
    command = request.json['command'].lower()
    dbid= request.json['dbid']
    result = subprocess.run(["bash","./rman.sh",connect_string, command, dbid] )
    print("result=", result)
    return jsonify({'result': 200}), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
