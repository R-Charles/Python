from flask_app import app
from flask import render_template, request, redirect, flash, session
from flask_app.models.planted_tree_model import Planted_tree, User


# @app.route( '/planted/<int:id>' )
# def display_planted_trees():
#     if 'email' not in session:
#         return redirect( '/' )
#     planted_trees_list = Planted_tree.get_all_with_users(request.form)    #Grab all the recipes
#     print (request.form)
#     return render_template( 'planted_trees_display.html', planted_trees_list = planted_trees_list )

# /new/show----shows_new.html----
@app.route( '/new' )
def display_create_planted():
    if 'email' not in session:
        return redirect( '/' )
    return render_template( "add_new.html" )

# /shows/new----/shows/new ------ /cars/new
@app.route( '/planted/new', methods = ['POST'] )
def create_planted():
    if Planted_tree.validate_planted_tree( request.form ) == False:  #validate fields
        return redirect( '/planted/new' )

    data = {
        **request.form,
        "user_id" : session['user_id']
    }

# /shows
    Planted_tree.create( data )
    return redirect( '/planted' )


# /shows ----- shows.html---/cars
@app.route('/planted')
def show_all():
    if 'user_id' not in session:
        return redirect( '/' )
    # data = {
    #     "id" : id
    # }
    planted_trees_list = Planted_tree.get_all_with_users()
    return render_template('dashboard2.html', planted_trees_list = planted_trees_list )

# @app.route( '/recipes' )
# def display_recipes():
#     if 'email' not in session:
#         return redirect( '/' )
#     list_recipes = Recipe.get_all_with_users()    #Grab all the recipes
#     return render_template( 'recipes.html', list_recipes = list_recipes )

# @app.route( '/edit/<int:id>' )
# @app.route( '/planted_trees/<int:id>/edit' )
# def display_one( id ):
#     if 'email' not in session:
#         return redirect( '/' )
#     data = {
#         "id" : id
#     }
#     current_car = Planted_tree.get_one_with_user( data )
#     return render_template( "dashboard.html", current_car = current_car )

# shows_display might want to CHANGE url 
@app.route( '/planted/<int:id>' )
def display_planted( id ):
    if 'email' not in session:
        return redirect( '/' )
    data = {
        "id" : id
    }
    current_planted_tree = Planted_tree.get_one_with_user( data )
    return render_template( "show2.html", current_planted_tree = current_planted_tree )

@app.route("/user/account")
def show_planted_trees():
    return render_template("show1.html",list_planted_trees= Planted_tree.get_with_user_planted_trees({"id":session["user_id"]}))


# watchout for potential error in f'... added cars to line 77
# @app.route( '/cars/edit/<int:id>', methods = ['POST'] ) was edit
@app.route( '/planted/<int:id>/update', methods = ['POST'] ) 
def update_planted( id ):
    if Planted_tree.validate_planted_tree( request.form ) == False:  #validate fields
        return redirect( f'/planted/{id}/edit' )
    planted_tree_data = {
        **request.form,
        "id": id,
    }
    Planted_tree.update_one( planted_tree_data)
    return redirect( '/planted' )


@app.route( '/planted/<int:id>/edit' ) 
def edit_planted(id):
    # if Planted_tree.validate_planted_tree( request.form ) == False:  #validate fields
    #     return redirect( '/' )
    data = {
    "id" : id
    }
    current_planted_tree = Planted_tree.get_one_with_user( data )
    return render_template( "edit2.html", current_planted_tree = current_planted_tree )


# /shows ----
@app.route( '/planted/<int:id>/delete' )
def delete_planted_tree( id ):
    data = {
        "id" : id 
    }
    Planted_tree.delete_one( data )
    return redirect( '/planted' )


