from myapp import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates


class Hero(db.Model, SerializerMixin):
    __tablename__ = "heroes"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    super_name = db.Column(db.String, unique = True, nullable = False)
    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())

    # powers = db.relationship("Power", secondary="hero_powers", backref="heroes_powers")

    # Serialization rules
    serialize_rules = ("-powers.heroes_powers",)

    def __repr__(self):
        return f"Hero {self.name} {self.super_name}"


class Power(db.Model, SerializerMixin):
    __tablename__ = "powers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())

    # heroes = db.relationship("Hero", secondary="hero_powers", back_populates="powers")

    # Serialization rules
    serialize_rules = ("-heroes.powers",)

    def __repr__(self):
        return f"Power {self.name}"

    # Validations for description attribute
    @validates("description")
    def validate_description(self, key, description):
        if len(description) > 250:
            raise ValueError("Description must be less than 250 characters")
        else:
            return description


class HeroPower(db.Model, SerializerMixin):
    __tablename__ = "hero_powers"

    id = db.Column(db.Integer, primary_key=True)
    hero_id = db.Column(db.Integer, db.ForeignKey("heroes.id"), nullable=False)
    hero = db.relationship("Hero", backref=db.backref("hero_powers", lazy=True))
    power_id = db.Column(db.Integer, db.ForeignKey("powers.id"), nullable=False)
    power = db.relationship("Power", backref=db.backref("hero_powers", lazy=True))
    strength = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())

    # Serialization rules
    serialize_rules = ("-hero.powers", "-power.heroes")

    def __repr__(self):
        return f" {self.hero_id} {self.power_id} {self.strength} "

    # Validations for strength attribute
    @validates("strength")
    def validate_strength(self, key, strength):
        if strength not in ["Strong", "Average", "Weak"]:
            raise ValueError("Strength must be either Strong, Average or Weak.")
        else:
            return strength
