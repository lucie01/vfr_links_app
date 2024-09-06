from flask import Blueprint, request, jsonify
from ..services.item_service import ItemService

class ItemController:
    def __init__(self):
        self.service = ItemService()
        self.blueprint = Blueprint('items', __name__)
        self.setup_routes()

    def setup_routes(self):
        @self.blueprint.route('/items', methods=['POST'])
        def create_item():
            try:
                data = request.json
                item_id = self.service.create_item(data)
                return jsonify({"success": True, "id": item_id}), 200
            except Exception as e:
                return jsonify({"error": str(e)}), 400

        @self.blueprint.route('/items/<id>', methods=['GET'])
        def get_item(id):
            try:
                item = self.service.get_item(id)
                if item:
                    return jsonify(item), 200
                else:
                    return jsonify({"error": "Item not found"}), 404
            except Exception as e:
                return jsonify({"error": str(e)}), 400

        @self.blueprint.route('/items/<id>', methods=['PATCH'])
        def update_item(id):
            try:
                data = request.json
                self.service.update_item(id, data)
                return jsonify({"success": True}), 200
            except Exception as e:
                return jsonify({"error": str(e)}), 400

        @self.blueprint.route('/items/<id>', methods=['DELETE'])
        def delete_item(id):
            try:
                self.service.delete_item(id)
                return jsonify({"success": True}), 200
            except Exception as e:
                return jsonify({"error": str(e)}), 400
