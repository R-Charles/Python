from unittest import result
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DATABASE
from flask_app.models.user_model import User

class Band:
    def __init__( self, data ):
        self.id = data['id']
        self.band_name = data['band_name']
        self.home_city = data['home_city']
        self.founding_member = data['founding_member']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.genre = data['genre']

    @classmethod
    def create( cls,data ):
        query = "INSERT INTO bands( band_name, home_city, genre, founding_member, user_id ) "
        query += "VALUES (%(band_name)s, %(home_city)s, %(genre)s, %(founding_member)s, %(user_id)s );"

        result = connectToMySQL( DATABASE ).query_db( query,data )
        print(result)
        return result
    
    @classmethod
    def get_all_with_users( cls ): ##***
        query = "SELECT * " 
        query += "FROM bands "
        query += "JOIN users ON bands.user_id = users.id;"

        results = connectToMySQL( DATABASE ).query_db( query ) ##***
        list_bands = []
        # print( results )
        for row in results:
            current_band = cls( row )
            user_data = {
                **row,
                "created_at" : row['users.created_at'],
                "updated_at" : row['users.updated_at'],
                "id" : row['users.id']
            }
            current_user = User( user_data )
            current_band.user = current_user
            list_bands.append( current_band )
        return list_bands

    @classmethod
    def get_band_from_users( cls ):
        query = "SELECT * "
        query += "FROM bands "
        query += "LEFT JOIN users ON bands.user_id = users.id;"
        results = connectToMySQL(DATABASE).query_db(query)
        if results:
            all_bands = []
            for bands in results:
                bands_actual = cls(bands)
                users_data = {
                    **bands,
                    'id': bands['users.id'],
                    'created_at': bands['users.created_at'],
                    'updated_at': bands['users.updated_at'],
                }
                user = User(users_data)
                bands_actual.user = user
                all_bands.append(bands_actual)
            return all_bands

    # @classmethod
    # def get_all_with_user( cls, data ): ##***
    #     query = "SELECT * " 
    #     query += "FROM bands "
    #     query += " WHERE bands.id = %(id)s;"

    #     result = connectToMySQL( DATABASE ).query_db( query, data )

    #     if len( result ) > 0: 
    #         list_band = cls( result[0] )
    #         user_data = {
                
    #             **result[0],
    #             "created_at" : result[0]['users.created_at'],
    #             "updated_at" : result[0]['users.updated_at'],
    #             "id" : result[0]['users.id'] 
            
    #         }
    #         list_band.user = User( user_data )
    #         return list_band
    #     else:
    #         return None

    @classmethod
    def get_with_user_bands(cls, data):
        query = "SELECT * "
        query += "FROM bands "
        query += "WHERE bands.user_id = %(id)s;"
        
        result= connectToMySQL(DATABASE).query_db(query, data )
        bands = []
        for row in result:
            bands.append(cls(row))
        return bands 

    @classmethod
    def get_one_with_user( cls, data ):
        query = " SELECT * " 
        query += " FROM bands "
        query += " JOIN users ON bands.user_id = users.id "
        query += " WHERE bands.id = %(id)s;"

        result = connectToMySQL( DATABASE ).query_db( query, data )

        if len( result ) > 0: 
            current_band = cls( result[0] )
            user_data = {
                
                **result[0],
                "created_at" : result[0]['users.created_at'],
                "updated_at" : result[0]['users.updated_at'],
                "id" : result[0]['users.id'] 
            
            }
            current_band.user = User( user_data )
            return current_band
        else:
            return None

    @classmethod
    def update_one( cls, data ):
        query = " UPDATE bands "
        query += "SET band_name = %(band_name)s, home_city = %(home_city)s, founding_member = %(founding_member)s, genre = %(genre)s "
        # query += "cooked_date = %(cooked_date)s, under_30 = %(under_30)s, "
        query += "WHERE id = %(id)s; "

        return connectToMySQL(DATABASE).query_db( query, data )

    @classmethod
    def delete_one( cls, data ):
        query = " DELETE FROM bands "
        query += "WHERE id = %(id)s;"
        return connectToMySQL( DATABASE ).query_db( query, data )


    @staticmethod
    def validate_band( data ):
        is_valid = True 
        if len(data["band_name"]) < 5:
            flash( "band_name must hold a minimum of 5 characters", "error_band_name" )
            is_valid = False 
        if data['founding_member'] == "":
            flash( "founding_member must not be empty", "error_band_founding_member" )
            is_valid = False 
        if len(data['home_city']) < 2:
            flash("home_city must be at least 2 characters.", "error_home_city")
            is_valid = False    
        if data['genre'] == '':
            flash( "Genre must not be empty", "error_band_genre" )
            is_valid = False 
        # if int(data['price']) < 0:
        #     flash( "Price must not be empty", "error_band_price" )
        #     is_valid = False 

        return is_valid



        # line 72 description may effect table data


