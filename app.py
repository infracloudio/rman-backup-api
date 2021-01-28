from flask import Flask,request,jsonify
import os 
import subprocess

app = Flask(__name__)

@app.route("/")
def helloWorld():
    return "Hello World\n"


@app.route("/echo/<text>")
def echoCommand(text):
    os.system("echo " +  text) 
    return "Command executed successfully\n"


@app.route("/rman", methods=['POST'])
def rmanCommand():
    if not request.json or not 'connect_string' in request.json:
        abort(400)
    connect_string = request.json['connect_string']
    command = request.json['command'].lower()
    if command in ['list','backupcontrolfile','fullbackup','restore']:
        result = subprocess.run(["bash","./rman.sh",connect_string, command] )
    else:
        return "invalid command"
    print("result=", result)
    return jsonify({'result': 200}), 200
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
