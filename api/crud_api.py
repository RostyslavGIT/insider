from api.request_client import SessionClientJSON

class CRUDAPI:
    def __init__(self, base_url: str):
        self.client = SessionClientJSON(base_url)


    def create_pet(self, pet_data: dict):
        return self.client.post("/pet", json=pet_data)


    def get_pet(self, pet_id: int):
        return self.client.get(f"/pet/{pet_id}")


    def update_pet(self, pet_data: dict):
        return self.client.put("/pet", json=pet_data)


    def delete_pet(self, pet_id: int):
        return self.client.delete(f"/pet/{pet_id}")