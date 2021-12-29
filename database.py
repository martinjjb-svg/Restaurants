from entities import Restaurant

class Database:

    def __init__(self):
        self.restaurants = []
        self.last_id = 0
        self.add_restaurant("Ivy City Garden", "London", "Modern")
        self.add_restaurant("Sushi Samba", "London", "Asian")

    def add_restaurant(self, name, address, nationality):
        new_restaurant = Restaurant(self.last_id, name, address, nationality)
        self.restaurants.append(new_restaurant)
        self.last_id += 1
        return new_restaurant.id

    def get_restaurant_by_id(self, id):
        for restaurant in self.restaurants:
            if restaurant.id == id:
                return restaurant
        return None

    def get_restaurant_by_name(self, name):
        for restaurant in self.restaurants:
            if restaurant.name == name:
                return restaurant
        return None

    def get_restaurant_by_address(self, address):
        for restaurant in self.restaurants:
            if restaurant.address == address:
                return restaurant
        return None

    def get_restaurant_by_nationality(self, nationality):
        nat = []
        for restaurant in self.restaurants:
            if restaurant.nationality == nationality:
                nat.append(restaurant.to_dict())
        return nat
