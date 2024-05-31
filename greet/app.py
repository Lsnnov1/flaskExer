from flask import Flask

app = Flask(__name__)
app.debug = True

@app.route('/welcome')
def welcome():
    return f"""
    <h1>Welcome</h1>
    <ul>
        <li><a href="/welcome/home">home</a></li>
        <li><a href="/welcome/back">back</a></li>
    </ul>
    """

@app.route("/welcome/home")
def welcome_home():
    return f"""
    <h1>Welcome Home</h1>
    <a href="/welcome">Welcome</a>
    """

@app.route("/welcome/back") 
def welcome_back():
    return f"""
    <h1>Welcome Back</h1>
    <a href="/welcome">Welcome</a>
    
"""