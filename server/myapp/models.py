from myapp import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates


class Hero(db.Model, SerializerMixin):
    __tablename__ = "heroes"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)

    hero_powers = db.relationship("HeroPower", back_populates="hero")

    # Serialization rules
    serialize_rules = ("-hero_powers.hero", "-hero_powers.power.hero_powers")


class Power(db.Model, SerializerMixin):
    __tablename__ = "powers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)

    hero_powers = db.relationship("HeroPower", back_populates="power")

    # Serialization rules
    serialize_rules = ("-hero_powers.power", "-hero_powers.hero")


class HeroPower(db.Model, SerializerMixin):
    __tablename__ = "hero_powers"

    id = db.Column(db.Integer, primary_key=True)
    hero_id = db.Column(db.Integer, db.ForeignKey("heroes.id"), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey("powers.id"), nullable=False)
    strength = db.Column(db.Integer, nullable=False)

    hero = db.relationship("Hero", back_populates="hero_powers")
    power = db.relationship("Power", back_populates="hero_powers")

    # Serialization rules
    serialize_rules = ("-hero.hero_powers", "-power.hero_powers")
