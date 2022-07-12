from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

list_of_users = [{
    "first_name" : "Alex",
    "last_name" : "Miller",
    "id" : 1
},
{
    "first_name" : "Martha",
    "last_name" : "Speaks",
    "id" : 2
},
{
    "first_name" : "Roger",
    "last_name" : "Anderson",
    "id" : 3
}]

list_of_todos = [{
    "description" : "Learn Python",
    "status" : "complete",
    "id" : 1,
    "user_id" : 1
},
{
    "description" : "List of OOP",
    "status" : "complete",
    "id" : 2,
    "user_id" : 1
},
{
    "description" : "Learn routes in Flask",
    "status" : "in_progress",
    "id" : 3,
    "user_id" : 2
},
{
    "description" : "Learn POST",
    "status" : "in_progress",
    "id" : 4,
    "user_id" : 3
}]


@app.route( '/todos' )          # The "@" decorator associates this route with the function immediately following
def get_todos():
    return render_template('todos.html', todos = list_of_todos)

@app.route('/todo/form')
def display_todo_form():
    return render_template( 'todo_form.html', users = list_of_users )

"""
Method: GET 
Getting all of a particular type
Url: '/todos'
Function: get_all_todos()
          get_todos()

Method: GET
Getting one of a particular type
Url: '/todo/<int:id>'
Function: get_todo_by_id( id )

Method: GET
Displaying a form for a type 
Url: '/todo/form'
Function: display_todo_form()
"""

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.