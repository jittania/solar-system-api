from app import db
from app.models.planet import Planet
from flask import request, Blueprint, make_response, jsonify

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")


@planets_bp.route("/<planet_id>", methods=["GET","PUT", "DELETE"], strict_slashes=False)
def handle_planet(planet_id):
    # Try to find the planet with the given id
    planet = Planet.query.get(planet_id)

    #=============================
    if planet is None:
        return make_response(f"Planet with id {planet_id} was not found", 404)
    #=============================

    if request.method == "GET": 
        return {
        "id": planet.id,
        "name": planet.name,
        "description": planet.description,
        "order": planet.order,
        }, 200

    elif request.method == "PUT":
        form_data = request.get_json()

        planet.name = form_data["name"]
        planet.description = form_data["description"]
        planet.order = form_data["order"]

        db.session.commit()

        return make_response(f"Planet #{planet.id} successfully updated")
    
    elif request.method == 'DELETE':
        db.session.delete(planet)
        db.session.commit()

        return make_response(f"Planet #{planet.id} successfully deleted")
    
    # return { #if the planet isn't found
    #     "message": f"Planet with id {planet_id} was not found",
    #     "success": False,
    #     }, 404


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

