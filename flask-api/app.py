#!flask/bin/python
from flask import Flask, jsonify, abort, request
import subprocess
import json
import parser
from subprocess import Popen, PIPE
from pprint import pprint

# from urllib.request import urlopen
app = Flask(__name__)

@app.route('/help', methods=['GET'])
def help():
    s = '''Welcome to Tempest, the Integration test Suite: \n
              Below are some of the commands for General and Generic Calls \n
              /general :  \n
              rally verify show \n 
              rally verify report \n
              rally deployment show    \n      
              /generic : \n
              rally deployment check cloudname \n
              rally deployment config cloudname    \n
              rally deployment use cloudname               
           ''' 
    return s

@app.route('/general', methods=['POST'])
def general():
    x = request.json
    print("action1 :", x["action1"])
    print("action2 :", x["action2"])
    cmd = ["rally",x['action1'],x['action2']]
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
    out,err = p.communicate()
    return out  

@app.route('/generic', methods=['POST'])
def generic():
    x = request.json
    print("action1 :", x["action1"])
    print("action2 :", x["action2"])
    print("cloud_name :", x["cloud_name"])
    cmd = ["rally",x['action1'],x['action2'],x['cloud_name']]
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
    out,err = p.communicate()
    return out  

@app.route('/report', methods=['GET','POST'])
def report():
    cmd = ["rally","verify","report","--uuid","557989c7-2306-4311-96f9-10c9449c46e7"]
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                              stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE)
    out,err = p.communicate()
    y = jsonify(out)
    for z in y:
      for item in z:
        print item.get("status", "null")
    # return jsonify(out)
    # return 




@app.route('/printing', methods=['GET'])
def printing():
    cmd = ["rally","verify","list"]
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                             stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
    out,err = p.communicate()
    return jsonify(out)

   
if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8080
        )
