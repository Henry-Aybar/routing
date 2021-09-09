from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          
def hello_world():
    return 'Hello World!'  

@app.route('/dojo')
def success():
    return 'Dojo'

@app.route('/say/<string:name>')
def say(name):
    return f"Hi {name}"

@app.route('/repeat/<int:num>/<string:name>')
def hello(num, name):
    return f"hello {num * name}"

if __name__=="__main__":  
    app.run(debug=True)    