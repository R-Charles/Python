from flask import flash
from flask_app import DATABASE
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import EMAIL_REGEX


class User:
    def __init__( self, data ):
        self.id = data['id']
        self.first_name = ['first_name']
        self.last_name = ['last_name']
        self.email = ['email']
        self.password = ['password']
        self.created_at = ['created_at']
        self.updated_at = ['updated_at']

    @classmethod
    def create( cls, data ):
        query = "INSERT INTO user( first_name, last_name, email, password ) "
        query += "VALUES ( %(first_name)s, %(last_name)s, %(email)s, %(password)s ); "

        result = connectToMySQL( DATABASE ).query_db( query, data )
        print(result)
        return result

    @classmethod
    def get_one_to_validate_email( cls, data ):
        query = "SELECT * "
        query += "FROM user "
        query += "WHERE email = %(email)s;"

        result = connectToMySQL( DATABASE ).query_db( query, data )

        
        if len( result ) > 0:
            current_user = cls( result[0] )
            return current_user
        else:
            return None

    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM users WHERE id=%(id)s"
        return connectToMySQL('sasquatch_sightings').query_db(query,data)

    # Other Burger methods up yonder.
    # Static methods don't have self or cls passed into the parameters.
    # We do need to take in a parameter to represent our burger
    @staticmethod
    def validate_user(data):
        is_valid = True # we assume this is true
        if len(data['first_name']) < 2:
            flash("first name must be at least 2 characters.", "error_registration_first_name")
            is_valid = False
        if len(data['last_name']) < 2:
            flash("last name must be at least 2 characters.", "error_registration_last_name")
            is_valid = False
        # if int(burger['calories']) < 200:
        #     flash("calories must be 200 or greater.")
        #     is_valid = False
        if not EMAIL_REGEX.match( data['email'] ):
            flash("Invalid email", "error_registration_email")
            is_valid = False
        if len(data['password']) < 8:
            flash("password must be at least 8 characters.", "error_registration_password" )
            is_valid = False
        if data['password'] != data['password_confirmation']:
            flash( "password does not match", "error_registration_password_confirmation")
            is_valid = False
        return is_valid