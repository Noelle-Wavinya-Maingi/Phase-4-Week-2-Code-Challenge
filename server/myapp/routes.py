from flask import make_response, jsonify, request, render_template
from myapp import api, db
from flask_restful import Resource
from myapp.models import Hero, Power, HeroPower

class Heroes(Resource):
    def get(self):
        
        try:
            heroes = Hero.query.all()

            heroes_list = [hero.to_dict() for hero in heroes]

            # response = make_response(jsonify(heroes_list), 200)

            return render_template("index.html", heroes = heroes_list)
        
        except Exception as e:
            error_message = str(e)
            return make_response(jsonify({"error": error_message}), 500)

class HeroesByID(Resource):
    def get(self, id):
        
        try:
            hero = Hero.query.filter_by(id = id).first()

            if hero:
                return render_template("index.html", hero = hero.to_dict())
            
            else:
                response_dict = {"error": "Hero not found"}
                response = make_response(response_dict, 404)

            return response
        
        except Exception as e:
            error_message = str(e)
            return make_response(jsonify({"error": error_message}), 500)
        
class Powers(Resource):
    def get(self):

         try:
            powers = Power.query.all()

            powers_list = [power.to_dict() for power in powers]

            return render_template("index.html", powers = powers_list)
        
         except Exception as e:
            error_message = str(e)
            return make_response(jsonify({"error": error_message}), 500)
         
class PowersByID(Resource):
    def get(self, id):
        
        try:
            power = Power.query.filter_by(id = id).first()

            if power:
                return render_template("index.html", power = power.to_dict())
            
            else:
                response_dict = {"error": "Power not found"}
                response = make_response(response_dict, 404)

            return response
        
        except Exception as e:
            error_message = str(e)
            return make_response(jsonify({"error": error_message}), 500)
        
    def patch(self, id):
            try:
                power = Power.query.get(id)

                if not power:
                    return {"error": "Power not found"}, 404

                data = request.get_json()  

                if "name" in data:
                    power.name = data["name"]

                if "description" in data:
                    power.description = data["description"]

                db.session.commit()

                response = make_response(power.to_dict(), 200)
                return response
               
            except Exception as e:
                error_message = str(e)
                return make_response(jsonify({"error": error_message}), 500)

class HerosPower(Resource):
    def get(self):

         try:
            heropower = HeroPower.query.all()

            powers_list = [power.to_dict() for power in heropower]

            return render_template("index.html", powers = powers_list)

        
         except Exception as e:
            error_message = str(e)
            return make_response(jsonify({"error": error_message}), 500)
         
    def post(self):
        try:
            data = request.get_json()

            strength = data.get("strength")
            power_id = data.get("power_id")
            hero_id = data.get("hero_id")

            if not strength or not power_id or not hero_id:
                return {"errors": ["validation errors"]}, 400
            
            power = Power.query.get(power_id)
            hero = Hero.query.get(hero_id)

            if not power or not hero:
                return {"errors": ["Power or Hero not found"]}, 404
            
            hero_power = HeroPower(strength = strength, power_id = power_id, hero_id = hero_id)

            db.session.add(hero_power)
            db.session.commit()

            hero_data = {
                "id": hero.id,
                "name": hero.name,
                "powers":[
                    {
                        "id": power.id,
                        "name": power.name,
                        "description": power.description,
                    }
                ],
            }

            return hero_data, 201
        
        except Exception as e:
            error_message = str(e)
            return make_response(jsonify({"error": error_message}), 500)
    
api.add_resource(Heroes, '/heroes')
api.add_resource(HeroesByID, '/heroes/<int:id>')
api.add_resource(Powers, '/powers')
api.add_resource(PowersByID, '/powers/<int:id>')
api.add_resource(HerosPower, '/hero_powers')