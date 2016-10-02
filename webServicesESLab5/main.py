#!flask/bin/python
from flask import Flask, jsonify, request

app = Flask(__name__)
from pprint import pprint as pprint
import json

@app.route('/', methods=['GET'])
def hello():
    return jsonify({'message': 'Please provide POST query to this server with var1, var2 and meth=(plus, minus, multiply, divide) parameters'})

@app.route('/', methods=['POST'])
def calc():
	response = ""
	req = json.loads(request.data)
	if checkVars(req):
		var1=int(req['var1'])
		var2=int(req['var2'])
		meth=str(req['meth'])
		if (req["meth"]=="plus"):
			summ = var1+var2
			response = str(var1) +" plus " + str(var2) + "=" + str(summ)
		elif (req["meth"]=="minus"):
			minus = var1-var2
			response = str(var1) +" minus " + str(var2) + "=" + str(minus)
		elif (req["meth"]=="multiply"):
			multiply = var1*var2
			response = str(var1) +" multiply " + str(var2) + "=" + str(multiply)
		elif (req["meth"]=="divide"):
			divide = var1/var2
			response = str(var1) +" divide " + str(var2) + "=" + str(divide)
		else:
			response = "Don't know that method " + meth
	else:
		response = "Check parameters"
	return jsonify({'message': response})

def checkVars(req):
	return req['var1'].isdigit() and req['var2'].isdigit() and req['meth']!= None

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True)