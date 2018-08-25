from flask import Flask,request, jsonify
import json
app = Flask(__name__)


@app.route("/")
def hello():
  return "hola mundo"

@app.route('/getData/<name>')
def getData(name):

  print (name)
  data = [[1, 2, 3], {"a": 1, "b": 2}, name]
  return json.dumps(data)

  #return jsonify(success=True, data=data)

@app.route('/data' ,  methods=['POST'])
def getDataFromFunction():

  a = request.get_json()

  print ("res: ",a)

  data = [[1,2,3],{"a":1,"b":2}, a]
  #return json.dumps("answer")
  return jsonify(success=True, data=data)

if __name__ == "__main__":
  app.run(host='localhost', port=5000, debug=True)
