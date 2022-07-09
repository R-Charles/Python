from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/python')
def display_python_message():
    return "Hello this is a different route /python"

@app.route('/hello/<name>')
def greet_person(name):
    print(f"hey there {name}")
    return f"Howdy, {name}"

@app.route('/info/<name>/<age>')
def display_info(name, age):
    print(type(name), type(age))
    return f"Name: {name} Age: {age}"
    
                           # Return the string 'Hello World!' as a response
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

