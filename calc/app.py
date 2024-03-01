from flask import Flask, request
import operations

app = Flask(__name__)

@app.route("/add")
def add():
    """add query inputs"""
    a = request.args["a"]
    b = request.args["b"]
    return str(operations.add(float(a),float(b)))

@app.route("/sub")
def sub():
    """subtract query inputs"""
    a = request.args["a"]
    b = request.args["b"]
    return str(operations.sub(float(a),float(b)))

@app.route("/mult")
def mult():
    """multiply query inputs"""
    a = request.args["a"]
    b = request.args["b"]
    return str(operations.mult(float(a),float(b)))

@app.route("/div")
def div():
    """divide query inputs"""
    a = request.args["a"]
    b = request.args["b"]
    return str(operations.div(float(a),float(b)))

@app.route("/math/<op>")
def math_op(op):
    """apply operation on query inputs"""
    a = request.args["a"]
    b = request.args["b"]
    ops = {"add": operations.add,
           "sub": operations.sub,
           "mult": operations.mult,
           "div":operations.div}
    return str(ops[op](float(a), float(b)))