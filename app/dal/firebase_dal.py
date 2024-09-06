from firebase_admin import credentials, firestore, initialize_app

class FirebaseDAL:
    def __init__(self):
        self.db = self.init_firebase()

    def init_firebase(self):
        # Initialize Firebase app with default credentials managed by GCP IAM
        initialize_app()
        return firestore.client()

    def create_item(self, item_id, item_data):
        self.db.collection('your_collection_name').document(item_id).set(item_data)

    def get_item(self, item_id):
        doc = self.db.collection('your_collection_name').document(item_id).get()
        return doc.to_dict() if doc.exists else None

    def update_item(self, item_id, item_data):
        self.db.collection('your_collection_name').document(item_id).update(item_data)

    def delete_item(self, item_id):
        self.db.collection('your_collection_name').document(item_id).delete()
