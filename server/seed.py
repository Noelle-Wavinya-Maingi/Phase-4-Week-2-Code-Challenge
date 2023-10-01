from myapp import app, db
from myapp.models import Hero, Power, HeroPower

with app.app_context():
    db.session.query(Hero).delete()
    db.session.query(Power).delete()
    db.session.query(HeroPower).delete()

    hero1 = Hero(name="Superman")
    hero2 = Hero(name="Batman")
    hero3 = Hero(name="Wonder Woman")
    hero4 = Hero(name="Flash")
    hero5 = Hero(name="Aquaman")

    print("Heroes seeded successfully")

    power1 = Power(name="Flight", description="Allows the hero to fly")
    power2 = Power(name="Super Strength", description="Provides superhuman strength")
    power3 = Power(
        name="Invisibility", description="Allows the hero to become invisible"
    )
    power4 = Power(name="Speed", description="Grants super speed")
    power5 = Power(name="Telepathy", description="Allows mind communication")

    print("Powers seeded successfully")

    heropower1 = HeroPower(hero=hero1, power=power1, strength=100)
    heropower2 = HeroPower(hero=hero4, power=power4, strength=89)
    heropower3 = HeroPower(hero=hero2, power=power2, strength=96)
    heropower4 = HeroPower(hero=hero3, power=power3, strength=85)
    heropower5 = HeroPower(hero=hero5, power=power5, strength=90)

    print("HeroPowers seeded successfully")

    db.session.add_all(
        [
            hero1,
            hero2,
            hero3,
            hero4,
            hero5,
            power1,
            power2,
            power3,
            power4,
            power5,
            heropower1,
            heropower2,
            heropower3,
            heropower4,
            heropower5,
        ]
    )

    db.session.commit()
