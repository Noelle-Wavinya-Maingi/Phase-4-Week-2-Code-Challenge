from myapp import db
from sqlalchemy_serializer import SerializerMixin


class Hero(db.Model, SerializerMixin):
    __tablename__ = "heroes"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)

    # powers = db.relationship("Power", secondary="hero_powers", backref="heroes_powers")

    # Serialization rules
    serialize_rules = ("-powers.heroes_powers",)

    def __repr__(self):
        return f"Hero {self.name}"


class Power(db.Model, SerializerMixin):
    __tablename__ = "powers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)

    # heroes = db.relationship("Hero", secondary="hero_powers", back_populates="powers")

    # Serialization rules
    serialize_rules = ("-heroes.powers",)

    def __repr__(self):
        return f"Power {self.name}"


class HeroPower(db.Model, SerializerMixin):
    __tablename__ = "hero_powers"

    id = db.Column(db.Integer, primary_key=True)
    hero_id = db.Column(db.Integer, db.ForeignKey("heroes.id"), nullable=False)
    hero = db.relationship("Hero", backref=db.backref("hero_powers", lazy=True))
    power_id = db.Column(db.Integer, db.ForeignKey("powers.id"), nullable=False)
    power = db.relationship("Power", backref=db.backref("hero_powers", lazy=True))
    strength = db.Column(db.Integer, nullable=False)

    # Serialization rules
    serialize_rules = ("-hero.powers", "-power.heroes")

    def __repr__(self):
        return f" {self.hero_id} {self.power_id} {self.strength} "
