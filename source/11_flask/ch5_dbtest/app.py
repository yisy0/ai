from flask import Flask, render_template
from database.repository import get_emp_list, get_emp

app = Flask(__name__)

@app.route('/')
def index():
    emp_list = get_emp_list()
    return render_template('index.html', emp_list=emp_list)
@app.route('/emp/<int:empno>') 
def emp(empno): 
    emp = get_emp(empno)
    return render_template('emp.html', emp=emp)