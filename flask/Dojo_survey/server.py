from flask import Flask, render_template, request, redirect, session  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = "MY SECRETS"


@app.route( '/')          # The "@" decorator associates this route with the function immediately following
def index():
    return render_template('index.html')

@app.route('/result')
def submit_page():
    return render_template('result.html')

@app.route('/result', methods=['post'])
def redirect_submit():
    session['name'] = request.form['name']
    session['locations'] = request.form['locations']
    session['favourite language'] = request.form['favourite language']
    session['comment'] = request.form['comment']
    return redirect ('/result')


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.