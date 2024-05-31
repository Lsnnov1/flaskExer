
# import flask methods
from flask import Flask, request
# import operations.py
from operations import add, sub, mult, div


app = Flask(__name__)

# CREATE ADD ROUTE
@app.route("/add")
def do_add():
    """Add a and b parameters."""
# get args, ignore if not present
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    # use operation.py method
    result = add(a, b)
    # return number as string 
    return str(result)


# CREATE SUBTRACT ROUTE
@app.route("/sub")
def do_sub():
    """Subtract and b parameters."""
# get args, ignore if not present
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    # use operation.py method
    result = sub(a, b)
# return number as string
    return str(result)


# CREATE MULTIPLY ROUTE
@app.route("/mult")
def do_mult():
    """Multiply a and b parameters."""
# get args, ignore if not present
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    # use operation.py method
    result = mult(a, b)
# return number as string
    return str(result)


# CREATE DIVISION ROUTE
@app.route("/div")
def do_div():
    """Divide a and b parameters."""
# get args, ignore if not present
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    # use operation.py method
    result = div(a, b)
# return number as string
    return str(result)

### PART TWO FOR NOTES

# operators = {
#         "add": add,
#         "sub": sub,
#         "mult": mult,
#         "div": div,
#         }

# @app.route("/math/<oper>")
# def do_math(oper):
#     """Do math on a and b."""

#     a = int(request.args.get("a"))
#     b = int(request.args.get("b"))
#     result = operators[oper](a, b)

#     return str(result)


