from flask import make_response, jsonify
from myapp import api
from flask_restful import Resource
from myapp.models import Hero

class Heroes(Resource):
    def get(self):
        
        try:
            heroes = Hero.query.all()

            heroes_list = [hero.to_dict() for hero in heroes]

            response = make_response(jsonify(heroes_list), 200)

            return response
        
        except Exception as e:
            error_message = str(e)
            return make_response(jsonify({"error": error_message}), 500)

class HeroesByID(Resource):
    def get(self, id):
        
        try:
            hero = Hero.query.filter_by(id = id).first()

            if hero:
                response = make_response(hero.to_dict(), 200)
            
            else:
                response_dict = {"error": "Hero not found"}
                response = make_response(response_dict, 404)

            return response
        
        except Exception as e:
            error_message = str(e)
            return make_response(jsonify({"error": error_message}), 500)

    
api.add_resource(Heroes, '/heroes')
api.add_resource(HeroesByID, '/heroes/<int:id>')