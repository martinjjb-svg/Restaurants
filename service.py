from database import Database  # Added import of Bookshop
from flask import jsonify, make_response
db = Database()


#  applies get_book_by_title method to bookshop database
def get_restaurant_by_name(name):
    restaurant = db.get_restaurant_by_name(name)
    if restaurant is None:
        return make_response(jsonify(message="Restaurant not found",
                                     category="failed"), 404)
    return make_response(jsonify(message="Found restaurant by name",
                                 category="success",
                                 data=restaurant.to_dict()), 200)


def get_restaurant_by_address(address):
    restaurant = db.get_restaurant_by_address(address)
    if restaurant is None:
        return make_response(jsonify(message="Address not found",
                                     category="failed"), 404)
    return make_response(jsonify(message="Found restaurant by address",
                                 category="success",
                                 data=restaurant.to_dict()), 200)
    # return json.dumps(book.to_dict())
    # remove all json.dumps with make-response and use html message numbers / in postman create tabs for each


def get_restaurant_by_nationality(nationality):
    data = db.get_restaurant_by_nationality(nationality)
    if not data:
        return make_response(jsonify(message="Nationality not found",
                                     category="failed"), 404)
    return make_response(jsonify(message="Found restaurant by nationality",
                                 category="success",
                                 data=data), 200)


def add_restaurant(name, address, nationality):
    restaurant = db.get_restaurant_by_name(name)
    if restaurant is None:
        restaurant_id = db.add_restaurant(name, address, nationality)
        response = {"id": restaurant_id,
                    "name": name,
                    "address": address,
                    "nationality": nationality
                    }
        return make_response(jsonify(message="New restaurant added",
                                     category="created",
                                     data=response), 201)
    else:
        print(restaurant.to_dict())
        return make_response(jsonify(message="Restaurant already exists",
                                     category="Not modified",
                                     data=restaurant.to_dict()), 304)
