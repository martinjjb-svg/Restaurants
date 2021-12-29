class Restaurant:

    def __init__(self, id, name, address, nationality):
        self.id = id
        self.name = name
        self.address = address
        self.nationality = nationality

    def to_dict(self):
        return {"id": self.id,
                "name": self.name,
                "address": self.address,
                "nationality": self.nationality
                }
