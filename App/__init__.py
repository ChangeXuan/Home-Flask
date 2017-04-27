from flask import Flask

def create_app():
	app = Flask(__name__)
	
	from .Main import main as main_blueprint
	app.register_blueprint(main_blueprint)
	
	from .MiniTask import miniTask as mini_blueprint
	app.register_blueprint(mini_blueprint)

	from .People import people as mini_blueprint
	app.register_blueprint(mini_blueprint)

	from .TestPort import testPort as mini_blueprint
	app.register_blueprint(mini_blueprint)
	
	return app
