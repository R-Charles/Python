from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():

    users = [
            {'First_Name' : 'Michael', 'Last_Name' : 'Choi', 'Full_Name' : 'Michael Choi'},
            {'First_Name' : 'John', 'Last_Name' : 'Supsupin', 'Full_Name' : 'John Supsupin'},
            {'First_Name' : 'Mark', 'Last_Name' : 'Guillen', 'Full_Name' : 'Mark Guillen'},
            {'First_Name' : 'KB', 'Last_Name' : 'Tonel', 'Full_Name' : 'KB Tonel'}
            ]


    return render_template("index.html", list=users)  # Return the string 'Hello World!' as a response
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
 


