from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Register routes
    from .routes import init_routes
    init_routes(app)
    
    return app
