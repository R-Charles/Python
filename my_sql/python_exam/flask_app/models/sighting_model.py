from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DATABASE
from flask_app.models.user_model import User

class Sighting:
    def __init__( self, data ):
        self.id = data['id']
        self.location = data['location']
        self.date_sighted = data['date_sighted']
        self.description = data['description']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.sightings = data['sightings']

    @classmethod
    def create( cls, data ):
        query = "INSERT INTO sightings( location, date_sighted, description, sightings, user_id ) "
        query += "VALUES (%(name)s, %(date_sighted)s, %(description)s, %(sightings)s, %(user_id)s );"

        result = connectToMySQL( DATABASE ).query_db( query,data )
        print(result)
        return result
    
    @classmethod
    def get_all_with_users( cls, data ):
        query = "SELECT * " 
        query += "FROM sightings "
        query += "JOIN users ON sightings.user_id = users.id;"

        results = connectToMySQL( DATABASE ).query_db( query, data )
        list_sightings = []
        # print( results )
        for row in results:
            current_sighting = cls( row )
            user_data = {
                **row,
                "created_at" : row['users.created_at'],
                "updated_at" : row['users.updated_at'],
                "id" : row['users.id']
            }
            current_user = User( user_data )
            current_sighting.user = current_user
            list_sightings.append( current_sighting )
        return list_sightings

    @classmethod
    def get_one_with_user( cls, data ):
        query = " SELECT * " 
        query += " FROM sightings "
        query += " JOIN users ON sightings.user_id = users.id "
        query += " WHERE sightings.id = %(id)s;"

        result = connectToMySQL( DATABASE ).query_db( query, data )

        if len( result ) > 0: 
            current_sighting = cls( result[0] )
            user_data = {
                
                **result[0],
                "created_at" : result[0]['users.created_at'],
                "updated_at" : result[0]['users.updated_at'],
                "id" : result[0]['users.id'] 
            
            }
            current_sighting.user = User( user_data )
            return current_sighting
        else:
            return None

    @classmethod
    def update_one( cls, data ):
        query = " UPDATE sightings "
        query += "SET location = %(location)s, date_sighted = %(date_sighted)s, description = %(description)s, "
        # query += "cooked_date = %(cooked_date)s, under_30 = %(under_30)s, "
        query += "WHERE id = %(id)s; "

        return connectToMySQL(DATABASE).query_db( query, data )

    @classmethod
    def delete_one( cls, data ):
        query = " DELETE FROM sightings "
        query += "WHERE id = %(id)s;"
        return connectToMySQL( DATABASE ).query_db( query, data )


    @staticmethod
    def validate_sighting( data ):
        is_valid = True 
        if data['location'] == "":
            flash( "location must not be empty", "error_sighting_location" )
            is_valid = False 
        if data['description'] == "":
            flash( "Description must not be empty", "error_sighting_description" )
            is_valid = False 
        if len(data['sightings']) == 0:
            flash( "Sightings must not be empty", "error_sighting_instructions" )
            is_valid = False 

        return is_valid