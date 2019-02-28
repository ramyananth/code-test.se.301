from flask import Flask
from sqlalchemy import *
import json
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from flask import request
import unittest 

app = Flask(__name__)
cors = CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:0911@127.0.0.1:5432/quant"
db = SQLAlchemy(app)


class employee(db.Model):
  id =  db.Column(db.Integer, primary_key=True) #Datatype : SERIAL
  empname = db.Column(db.String(20))
  compname = db.Column(db.String(20))

  def __init__(self,emp,comp):
  	self.empname = emp
  	self.compname = comp
		

@app.route("/")
def home():
	d ={}
	for emp in employee.query.distinct(employee.compname):
		d[emp.compname] = employee.query.filter(employee.compname == emp.compname).count()
	return json.dumps(d)

@app.route("/insertData", methods=['GET', 'POST'])
def insert():
	if request.method == "POST":
		data = json.loads(request.data)
		print(data['employeName'])
		emp = employee(data['employeName'],data['company'])
		db.session.add(emp)
		db.session.commit()
		return('201')
	# emp = employee()

class TestData(unittest.TestCase):
	def databaseConnect(self):
		ans = home()
		print(ans)

if __name__ == '__main__':
   app.run()