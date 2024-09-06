from flask import request, jsonify
from .services.item_service import ItemService

def init_routes(app):
    item_service = ItemService()
    
    @app.route('/items', methods=['POST'])
    def create_item():
        try:
            data = request.json
            item_id = item_service.create_item(data)
            return jsonify({"success": True, "id": item_id}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    @app.route('/items/<id>', methods=['GET'])
    def get_item(id):
        try:
            item = item_service.get_item(id)
            if item:
                return jsonify(item), 200
            else:
                return jsonify({"error": "Item not found"}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    @app.route('/items/<id>', methods=['PATCH'])
    def update_item(id):
        try:
            data = request.json
            item_service.update_item(id, data)
            return jsonify({"success": True}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    @app.route('/items/<id>', methods=['DELETE'])
    def delete_item(id):
        try:
            item_service.delete_item(id)
            return jsonify({"success": True}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 400
