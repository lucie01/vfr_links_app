from flask import Flask
from app.controllers.item_controller import ItemController

app = Flask(__name__)

# Register the item routes
item_controller = ItemController()
app.register_blueprint(item_controller.blueprint)

if __name__ == '__main__':
    app.run(debug=True)
