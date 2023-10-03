from myapp import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

class Hero(db.Model, SerializerMixin):
    __tablename__ = "heroes"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    super_name = db.Column(db.String, unique=True, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # Relationship to HeroPower
    hero_powers = db.relationship("HeroPower", back_populates="hero")

    def __repr__(self):
        return f"Hero {self.name} {self.super_name}"

    # Serialization rules
    serialize_rules = ("-hero_powers.hero",)

class Power(db.Model, SerializerMixin):
    __tablename__ = "powers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # Relationship to HeroPower
    hero_powers = db.relationship("HeroPower", back_populates="power")

    def __repr__(self):
        return f"Power {self.name}"

    # Validations for description attribute
    @validates("description")
    def validate_description(self, key, description):
        if len(description) > 250:
            raise ValueError("Description must be less than 250 characters")
        else:
            return description

    # Serialization rules
    serialize_rules = ("-hero_powers.power",)

class HeroPower(db.Model, SerializerMixin):
    __tablename__ = "hero_powers"

    id = db.Column(db.Integer, primary_key=True)
    hero_id = db.Column(db.Integer, db.ForeignKey("heroes.id"), nullable=False)
    hero = db.relationship("Hero", back_populates="hero_powers")
    power_id = db.Column(db.Integer, db.ForeignKey("powers.id"), nullable=False)
    power = db.relationship("Power", back_populates="hero_powers")
    strength = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f"{self.hero_id} {self.power_id} {self.strength}"

    # Validation for strength attribute
    @validates("strength")
    def validate_strength(self, key, strength):
        if strength not in [1, 2, 3]:  # Use 1 for 'Weak', 2 for 'Average', 3 for 'Strong'
            raise ValueError("Strength must be either 1 for 'Weak', 2 for 'Average', or 3 for 'Strong'")
        else:
            return strength

    # Serialization rules
    serialize_rules = ("-hero.hero_powers", "-power.hero_powers")
