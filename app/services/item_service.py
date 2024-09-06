from ..models.item import Profile
from ..dal.firebase_dal import FirebaseDAL

class ItemService:
    def __init__(self):
        self.dal = FirebaseDAL()

    def create_item(self, data):
        # Validate and create a Profile instance using Pydantic
        profile = Profile(**data)
        self.dal.create_item(profile.id, profile.dict())
        return profile.id

    def get_item(self, item_id):
        data = self.dal.get_item(item_id)
        if data:
            profile = Profile(**data)  # Reconstruct the Profile object
            return profile.dict()  # Convert to dict to return JSON response
        return None

    def update_item(self, item_id, data):
        existing_data = self.get_item(item_id)
        if existing_data:
            # Use the Pydantic model to update only valid fields
            updated_profile = Profile(**existing_data).copy(update=data)
            self.dal.update_item(item_id, updated_profile.dict())

    def delete_item(self, item_id):
        self.dal.delete_item(item_id)
