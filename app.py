from flask import Flask, request, jsonify, make_response
import json
import service
app = Flask(__name__)


@app.route("/")
def index():
    return "This is the index page for The B Best Restaurant Guide"


@app.route("/restaurant", methods=['POST', 'GET', 'PUT'])
def restaurants():

    if request.method == 'GET':
        type = request.json["type"]
        info = request.json["info"]

        if type == "name":
            return service.get_restaurant_by_name(info)

        if type == "address":
            return service.get_restaurant_by_address(info)

        if type == "nationality":
            return service.get_restaurant_by_nationality(info)

    if request.method == 'POST':
        name = request.json["name"]  # creates name equal to the value input next to the title key in json
        address = request.json["address"]
        nationality = request.json["nationality"]
        return service.add_restaurant(name, address, nationality)


if __name__ == '__main__':
    app.run()
