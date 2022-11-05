from unittest import result
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DATABASE
from flask_app.models.user_model import User

class Planted_tree:
    def __init__( self, data ):
        self.id = data['id']
        self.species = data['species']
        self.location = data['location']
        self.reason = data['reason']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.date_planted = data['date_planted']

    @classmethod
    def create( cls,data ):
        query = "INSERT INTO planted_trees( species, location, reason, date_planted, user_id ) "
        query += "VALUES (%(species)s, %(location)s, %(reason)s, %(date_planted)s, %(user_id)s );"

        result = connectToMySQL( DATABASE ).query_db( query,data )
        print(result)
        return result
    
    @classmethod
    def get_all_with_users( cls ): ##***
        query = "SELECT * " 
        query += "FROM planted_trees "
        query += "JOIN users ON planted_trees.user_id = users.id;"

        results = connectToMySQL( DATABASE ).query_db( query ) ##***
        list_planted_trees = []
        # print( results )
        for row in results:
            current_planted_tree = cls( row )
            user_data = {
                **row,
                "created_at" : row['users.created_at'],
                "updated_at" : row['users.updated_at'],
                "id" : row['users.id']
            }
            current_user = User( user_data )
            current_planted_tree.user = current_user
            list_planted_trees.append( current_planted_tree )
        return list_planted_trees

    @classmethod
    def get_planted_tree_from_users( cls ):
        query = "SELECT * "
        query += "FROM planted_trees "
        query += "LEFT JOIN users ON planted_trees.user_id = users.id;"
        results = connectToMySQL(DATABASE).query_db(query)
        if results:
            all_planted_trees = []
            for planted_trees in results:
                planted_trees_actual = cls(planted_trees)
                users_data = {
                    **planted_trees,
                    'id': planted_trees['users.id'],
                    'created_at': planted_trees['users.created_at'],
                    'updated_at': planted_trees['users.updated_at'],
                }
                user = User(users_data)
                planted_trees_actual.user = user
                all_planted_trees.append(planted_trees_actual)
            return all_planted_trees

    # @classmethod
    # def get_all_with_user( cls, data ): ##***
    #     query = "SELECT * " 
    #     query += "FROM planted_trees "
    #     query += " WHERE planted_trees.id = %(id)s;"

    #     result = connectToMySQL( DATABASE ).query_db( query, data )

    #     if len( result ) > 0: 
    #         list_planted_tree = cls( result[0] )
    #         user_data = {
                
    #             **result[0],
    #             "created_at" : result[0]['users.created_at'],
    #             "updated_at" : result[0]['users.updated_at'],
    #             "id" : result[0]['users.id'] 
            
    #         }
    #         list_planted_tree.user = User( user_data )
    #         return list_planted_tree
    #     else:
    #         return None

    @classmethod
    def get_with_user_planted_trees(cls, data):
        query = "SELECT * "
        query += "FROM planted_trees "
        query += "WHERE planted_trees.user_id = %(id)s;"
        
        result= connectToMySQL(DATABASE).query_db(query, data )
        planted_trees = []
        for row in result:
            planted_trees.append(cls(row))
        return planted_trees 

    @classmethod
    def get_one_with_user( cls, data ):
        query = " SELECT * " 
        query += " FROM planted_trees "
        query += " JOIN users ON planted_trees.user_id = users.id "
        query += " WHERE planted_trees.id = %(id)s;"

        result = connectToMySQL( DATABASE ).query_db( query, data )

        if len( result ) > 0: 
            current_planted_tree = cls( result[0] )
            user_data = {
                
                **result[0],
                "created_at" : result[0]['users.created_at'],
                "updated_at" : result[0]['users.updated_at'],
                "id" : result[0]['users.id'] 
            
            }
            current_planted_tree.user = User( user_data )
            return current_planted_tree
        else:
            return None

    @classmethod
    def update_one( cls, data ):
        query = " UPDATE planted_trees "
        query += "SET species = %(species)s, location = %(location)s, reason = %(reason)s, date_planted = %(date_planted)s"
        # query += "cooked_date = %(cooked_date)s, under_30 = %(under_30)s, "
        query += "WHERE id = %(id)s; "

        return connectToMySQL(DATABASE).query_db( query, data )

    @classmethod
    def delete_one( cls, data ):
        query = " DELETE FROM planted_trees "
        query += "WHERE id = %(id)s;"
        return connectToMySQL( DATABASE ).query_db( query, data )


    @staticmethod
    def validate_planted_tree( data ):
        is_valid = True 
        if len(data["species"]) < 5:
            flash( "Species must hold a minimum of 5 characters", "error_planted_tree_species" )
            is_valid = False 
        if len(data['reason']) > 51:
            flash( "Reason must not be empty", "error_planted_tree_reason" )
            is_valid = False 
        if len(data['location']) < 2:
            flash("location must be at least 2 characters.", "error_location")
            is_valid = False    
        if data['date_planted'] == '':
            flash( "date_planted must not be empty", "error_planted_tree_date" )
            is_valid = False 
        # if int(data['price']) < 0:
        #     flash( "Price must not be empty", "error_planted_tree_price" )
        #     is_valid = False 

        return is_valid



        # line 72 description may effect table data


