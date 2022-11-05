from flask_app import app   
from flask_app.controllers import planted_trees_controller, users_controller


if __name__ == "__main__":
    app.run(debug = True)

