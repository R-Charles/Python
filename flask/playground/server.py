from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def play():
    return render_template("play.html", color="red")

@app.route('/<int:num>')          # The "@" decorator associates this route with the function immediately following
def box_range(num):
    return render_template("play.html", num=num)

@app.route('/<int:num>/<string:color>')          # The "@" decorator associates this route with the function immediately following
def box_color(color, num):
    return render_template("play.html", color=color, num=num)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

