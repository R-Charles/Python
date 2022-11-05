from flask_app import app
from flask import render_template, request, redirect, flash, session
from flask_app.models.sighting_model import Sighting


@app.route( '/dashboard' )
def display_dashboard():
    if 'email' not in session:
        return redirect( '/' )
    sightings_list = Sighting.get_all_with_users(request.form)    #Grab all the recipes
    print (request.form)
    return render_template( 'dashboard.html', sightings_list = sightings_list )

@app.route( '/new/sighting' )
def display_create_sighting():
    if 'email' not in session:
        return redirect( '/' )
    return render_template( "new_sighting.html" )

@app.route( '/new/sighting', methods = ['POST'] )
def create_sighting():
    if Sighting.validate_sighting( request.form ) == False:  #validate fields
        return redirect( '/new/sighting' )

    data = {
        **request.form,
        "user_id" : session['user_id']
    }

    Sighting.create( data )
    return redirect( '/dashboard' )

@app.route( '/edit/<int:id>' )
def display_one( id ):
    if 'email' not in session:
        return redirect( '/' )
    data = {
        "id" : id
    }
    current_sighting = Sighting.get_one_with_user( data )
    return render_template( "dashboard.html", current_sighting = current_sighting )

@app.route( '/show/<int:id>' )
def display_sighting( id ):
    if 'email' not in session:
        return redirect( '/' )
    data = {
        "id" : id
    }
    current_sighting = Sighting.get_one_with_user( data )
    return render_template( "show.html", current_sighting = current_sighting )


@app.route( '/edit/<int:id>', methods = ['POST'] )
def update_sighting( id ):
    if Sighting.validate_sighting( request.form ) == False:  #validate fields
        return redirect( f'/dashboard/{id}/update' )
    sighting_data = {
        **request.form,
        "id": id,
    }
    Sighting.update_one( sighting_data)
    return redirect( '/dashboard' )

@app.route( '/dashboard/<int:id>/delete' )
def delete_sighting( id ):
    data = {
        "id" : id 
    }
    Sighting.delete_one( data )
    return redirect( '/dashboard' )

