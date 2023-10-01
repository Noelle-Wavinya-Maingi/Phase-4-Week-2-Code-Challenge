from myapp import app, db
from myapp.models import Hero, Power, HeroPower

if __name__ == "__main__":
    app.run(debug=True, port=5555)