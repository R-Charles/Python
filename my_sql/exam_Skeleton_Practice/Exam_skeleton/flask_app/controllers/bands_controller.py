from flask_app import app
from flask import render_template, request, redirect, flash, session
from flask_app.models.band_model import Band, User



# /new/show----shows_new.html----
@app.route( '/new/sighting' )
def display_create_band():
    if 'email' not in session:
        return redirect( '/' )
    return render_template( "add_new.html" )

# /shows/new----/shows/new ------ /cars/new
@app.route( '/band/new', methods = ['POST'] )
def create_band():
    if Band.validate_band( request.form ) == False:  #validate fields
        return redirect( '/band/new' )

    data = {
        **request.form,
        "user_id" : session['user_id']
    }

    Band.create( data )
    return redirect( '/band' )


# /shows ----- shows.html---/cars
@app.route('/band')
def show_all():
    if 'user_id' not in session:
        return redirect( '/' )
    # data = {
    #     "id" : id
    # }
    bands_list = Band.get_all_with_users()
    return render_template('dashboard2.html', bands_list = bands_list )

# @app.route( '/recipes' )
# def display_recipes():
#     if 'email' not in session:
#         return redirect( '/' )
#     list_recipes = Recipe.get_all_with_users()    #Grab all the recipes
#     return render_template( 'recipes.html', list_recipes = list_recipes )

#**************************************************
# shows_display might want to CHANGE url 
# @app.route( '/band/<int:id>' )
# def display_band( id ):
#     if 'email' not in session:
#         return redirect( '/' )
#     data = {
#         "id" : id
#     }
#     current_band = Band.get_one_with_user( data )
#     return render_template( "show2.html", current_band = current_band )

@app.route("/mybands")
def show_bands():
    return render_template("show1.html",list_bands= Band.get_with_user_bands({"id":session["user_id"]}))


# watchout for potential error in f'... added cars to line 77
# @app.route( '/cars/edit/<int:id>', methods = ['POST'] ) was edit
@app.route( '/band/update/<int:id>', methods = ['POST'] ) 
def update_band( id ):
    if Band.validate_band( request.form ) == False:  #validate fields
        return redirect( f'/band/{id}/edit' )
    band_data = {
        **request.form,
        "id": id,
    }
    Band.update_one( band_data)
    return redirect( '/band' )


@app.route( '/band/<int:id>/edit' ) 
def edit_band(id):
    # if Band.validate_band( request.form ) == False:  #validate fields
    #     return redirect( '/' )
    data = {
    "id" : id
    }
    current_band = Band.get_one_with_user( data )
    return render_template( "edit2.html", current_band = current_band )


# /shows ----
@app.route( '/band/<int:id>/delete' )
def delete_band( id ):
    data = {
        "id" : id 
    }
    Band.delete_one( data )
    return redirect( '/band' )


