from typing import Counter
from flask import Flask, render_template, redirect, session  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = "MY SECRETS"


@app.route( '/counter' )          # The "@" decorator associates this route with the function immediately following
def counter():
    if 'count' in session:
        session['count'] += 1
        print('key exists!')
    else:
        session['count'] = 1

    return render_template('/counter.html')


@app.route('/destroy_session' )
def destroy():
    session.clear()
    return redirect('/counter')


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.