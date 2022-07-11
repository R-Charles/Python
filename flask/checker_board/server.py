# Import Flask to allow us to create our app
from flask import Flask, render_template
# Create a new instance of the Flask class called "app"
app = Flask(__name__)


# The "@" decorator associates this route with the function immediately following
@app.route('/')
def hello_world():
    # Return the string 'Hello World!' as a response
    return render_template('index_8x8.html')


# The "@" decorator associates this route with the function immediately following
@app.route('/8x8b')
def hello_world1():
    # Return the string 'Hello World!' as a response
    return render_template('index_8x8b.html')

# The "@" decorator associates this route with the function immediately following
@app.route('/8x4')
def hello_world2():
    # Return the string 'Hello World!' as a response
    return render_template('index_8x4.html')

# The "@" decorator associates this route with the function immediately following
@app.route('/8x4b')
def hello_world3():
    # Return the string 'Hello World!' as a response
    return render_template('index_8x4b.html')

# The "@" decorator associates this route with the function immediately following
@app.route('/10x10')
def hello_world4():
    # Return the string 'Hello World!' as a response
    return render_template('index_10x10.html')

# The "@" decorator associates this route with the function immediately following
@app.route('/10x10b')
def hello_world5():
    # Return the string 'Hello World!' as a response
    return render_template('index_10x10b.html')


if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
