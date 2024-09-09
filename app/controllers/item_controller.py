# app/controllers/item_controller.py

from flask import Blueprint, request, jsonify
from firebase_admin import firestore
from pydantic import ValidationError
from app.models.item import Profile
import uuid
from flask_cors import CORS  # Import CORS

class ItemController:
    def __init__(self):
        self.blueprint = Blueprint('items', __name__)
        CORS(self.blueprint, resources={r"/items/*": {"origins": "https://vfr-links-995250867468.europe-west1.run.app/"}})  # Allow only specific origin
        self.collection_name = 'links'  # Replace with your actual collection name
        self.collection_ref = firestore.client().collection(self.collection_name)

        # Define routes
        self.blueprint.add_url_rule('/items', view_func=self.create_item, methods=['POST'])
        self.blueprint.add_url_rule('/items/<id>', view_func=self.get_item, methods=['GET'])
        self.blueprint.add_url_rule('/items/<id>', view_func=self.update_item, methods=['PATCH'])
        self.blueprint.add_url_rule('/items/<id>', view_func=self.delete_item, methods=['DELETE'])

    def create_item(self):
        try:
            # Validate the request data against the Profile model
            data = request.json
            profile = Profile(**data)  # Pydantic validation

            # Convert profile data to a dictionary and ensure URL fields are strings
            profile_dict = profile.dict()
            profile_dict['id'] = str(uuid.uuid4())

            # Convert URLs to strings for Firestore compatibility
            profile_dict['avatar'] = str(profile_dict['avatar'])  # Convert avatar URL

            for link in profile_dict['links']:
                link['href'] = str(link['href'])  # Convert href URL
                if 'image' in link and link['image']:
                    link['image'] = str(link['image'])  # Convert image URL

            for social in profile_dict['socials']:
                social['href'] = str(social['href'])  # Convert social href URL

            # Save to Firestore
            self.collection_ref.document(profile_dict['id']).set(profile_dict)
            return jsonify({"success": True, "id": profile_dict['id']}), 200

        except ValidationError as e:
            return jsonify({"error": e.errors()}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    def get_item(self, id):
        try:
            doc = self.collection_ref.document(id).get()
            if doc.exists:
                return jsonify(doc.to_dict()), 200
            else:
                return jsonify({"error": "Item not found"}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    def update_item(self, id):
        try:
            data = request.json
            self.collection_ref.document(id).update(data)
            return jsonify({"success": True}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    def delete_item(self, id):
        try:
            self.collection_ref.document(id).delete()
            return jsonify({"success": True}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 400
