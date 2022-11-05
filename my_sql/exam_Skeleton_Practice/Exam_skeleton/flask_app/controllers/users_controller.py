from pickle import NONE
import re

# import bcrypt
from flask_app.models.user_model import User
from flask_app import app
from flask import render_template, session, redirect, request, flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
# from flask_app.models.user_model import user_model ****

@app.route('/') #works
def login():
    return render_template( 'login.html' )
    # if not user_model.validate_user_model(request.form):
    #     # we redirect to the template with the form.
    #     return redirect( '/' )
    # #... do other things
    # return redirect('/shows')


@app.route( '/user/create', methods = ['POST'] )
def registration():
    if User.validate_user( request.form ) == False:
        return redirect( '/' )
    data = {"email":request.form["email"]}

    user_exists = User.get_one_to_validate_email( data )
    if user_exists != None:
        flash( "This email already exists!", "error_registration_email" )
        return redirect( '/' )
    # proceed to create the user
    data = {
        **request.form,
        "password" : bcrypt.generate_password_hash( request.form['password'] )
    }
    user_id = User.create( data )
    
    session['first_name'] = data['first_name']
    session['last_name'] = data['last_name']
    session['email'] = data['email']
    session['user_id'] = user_id
#fix shows url
    return redirect( '/band' ) #This needs to change to another display route ('/user/welcome') ---/cars----

@app.route('/user/login', methods = ['POST']) ##******************##
def logon():
    current_user = User.get_one_to_validate_email( request.form )
    # was NONE
    if current_user:
        if not bcrypt.check_password_hash(current_user.password, request.form['password']):
            flash("Wrong credentials", "error_login_credentials")
            return redirect('/')
        session['first_name'] = current_user.first_name
        session['email'] = current_user.email
        session['user_id'] = current_user.id
        return redirect('/band')
    else:
        flash("Wrong credentials", "error_login_credentials")
        return redirect('/')


# @app.route('/user/login', methods = ['POST'])
# def logon():
#     current_user = User.get_one_to_validate_email(request.form)
#     if current_user != None:
#         if not bcrypt.check_password_hash(current_user.password, request.form['password']):
#             flash("Wrong credentials", "error_login_credentials")
#             return redirect('/')
#         session['first_name'] = current_user.first_name
#         session['email'] = current_user.email
#         session['user_id'] = current_user.id
#         return redirect('/shows')
#     else:
#         flash("Wrong credentials", "error_login_credentials")
#         return redirect('/')


# @app.route( '/user/process', methods = ['POST'] )
# def process():
#     pass

# @app.route( '/user/welcome' )
# def welcome():
#     return render_template( 'welcome.html' )

@app.route( '/user/logout')
def logout():
    session.clear()
    return redirect( '/' )



    # if current_user:
    #     if not bcrypt.check_password_hash(current_user["password"], request.form['password']):
    #         flash("Improper Credentials", "error_improper_credentials")
    #         return redirect( '/' )
    #     session['first_name'] = current_user["first_name"]
    #     session['last_name'] = current_user["last_name"]
    #     session['email'] = current_user["email"]
    #     session['user_id'] = current_user.id
    #     return redirect( '/band' )   #('/user/welcome')
    # else: 
    #     flash("uh oh", "spaghetti")
    #     return redirect( '/' )