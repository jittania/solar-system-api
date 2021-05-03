from app import db
from app.models.planet import Planet
from flask import request, Blueprint, make_response, jsonify

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")


@planets_bp.route("/<planet_id>", methods=["GET"], strict_slashes=False)
def handle_planet(planet_id):
    # Try to find the planet with the given id
    planet = Planet.query.get(planet_id)

    if planet: #if it's True
        return {
        "id": planet.id,
        "name": planet.name,
        "description": planet.description,
        "order": planet.order,
        }, 200
    
    return { #if the planet isn't found
        "message": f"Planet with id {planet_id} was not found",
        "success": False,
        }, 404


@planets_bp.route("", methods=["POST", "GET"])

def planets():
    if request.method == "GET":
        planets = Planet.query.all()
        planets_response = []
        for planet in planets:
            planets_response.append({
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "order": planet.order
            })
        return jsonify(planets_response), 200

    else:
        request_body = request.get_json()
        new_planet = Planet(name = request_body["name"],
                    description = request_body["description"],
                    order = request_body["order"])

    # add this model to the database. Commit these changes and make it happen
    db.session.add(new_planet)
    db.session.commit()

    return (f"Planet {new_planet.name} successfully created"), 201

