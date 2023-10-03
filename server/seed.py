from myapp import app, db
from myapp.models import Hero, Power, HeroPower

with app.app_context():
    db.session.query(Hero).delete()
    db.session.query(Power).delete()
    db.session.query(HeroPower).delete()

    hero1 = Hero(name="Kamala Khan", super_name='Ms Marvel')
    hero2 = Hero(name="Doreen Green", super_name="Squirrel Girl")
    hero3 = Hero(name="Gwen Stacy", super_name="Spider-Gwen")
    hero4 = Hero(name="Janet Van Dyne", super_name="The Wasp")
    hero5 = Hero(name="Wanda Maximoff", super_name="Scarlet Witch")
    hero6 = Hero(name="Carol Danvers", super_name="Captain Marvel")
    hero7 = Hero(name="Jean Grey", super_name="Dark Phoenix")
    hero8 = Hero(name="Ororo Munroe", super_name="Storm")
    hero9 = Hero(name="Kitty Pryde", super_name="Shadowcat")
    hero10 = Hero(name="Elektra Natchios", super_name="Elektra")

    print("Heroes seeded successfully")

    power1 = Power(name="Flight", description="Gives the wielder the ability to fly through the skies at supersonic speed")
    power2 = Power(name="Super Strength", description="Gives the wielder super-human strengths")
    power3 = Power(name="Invisibility", description="Allows the hero to become invisible")
    power4 = Power(name="Speed", description="Grants super speed")
    power5 = Power(name="Telepathy", description="Allows mind communication")

    print("Powers seeded successfully")

    heropower1 = HeroPower(hero=hero1, power=power1, strength=3)  # 'Strong'
    heropower2 = HeroPower(hero=hero4, power=power4, strength=2)  # 'Average'
    heropower3 = HeroPower(hero=hero2, power=power2, strength=1)  # 'Weak'
    heropower4 = HeroPower(hero=hero3, power=power3, strength=3)  # 'Strong'
    heropower5 = HeroPower(hero=hero5, power=power5, strength=1)  # 'Weak'

    print("HeroPowers seeded successfully")

    db.session.add_all(
        [
            hero1,
            hero2,
            hero3,
            hero4,
            hero5,
            hero6,
            hero7,
            hero8,
            hero9,
            hero10,
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
