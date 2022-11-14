"""
Container module for the butler weapons.
"""

class WeaponObject(object):

    def __init__(self, name='DEFAULT', descript='DEFAULT'):
        self.name = name
        self.descript = descript


strikingMartialArts = WeaponObject('Striking Martial Arts', 'You use Karate, Boxing, Muay Thai, Kung Fu, Capoeira or some other striking martial art to attack.')
grapplingMartialArts = WeaponObject('Grappling Martial Arts', 'You use Jujutsu, Aikido, Judo, or some other grappling/joint locking martial art to attack.')
securityWeapon = WeaponObject('Security', 'You can use the traps and other security devices installed all throughout the mansion to attack.')
tank = WeaponObject('Tank', 'You use your favorite tank to blast or run over your enemies.')
combatHelicopter = WeaponObject('Combat Helicopter', 'You use your favorite combat helicopter to shoot or bombard your enemies.')
tortureImplements = WeaponObject('Torture Implements', 'Torture implements that are awful just to look at. Fingernail pullers, the iron maiden, finger crushers, etc.')
handgun = WeaponObject('Handgun', 'A revolver, derringer, automatic pistol, or other handgun.')
machineGun = WeaponObject('Machinegun', 'A machinegun that can throw out a rain of bullets in a short period of time.')
rifle = WeaponObject('Rifle', 'An assault rifle, shotgun, musket, etc.')
bomb = WeaponObject('Bomb/Grenade', 'You use bombs, grenades, or maybe plastic explosives.')
bazooka = WeaponObject('Bazooka', 'When a fight breaks out you pull out a big-ass bazooka.')
rayGun = WeaponObject('Ray Gun', "It might look like a prop of a 50s sci-fi B movie, but the ray gun you're packing really does hurt people.")
devilPower = WeaponObject('Devil Power', 'Your physical body, fused with a demon, is a weapon in itself. You use this overwhelming, superhuman power to crush your foes. How it works exactly is up to you.')
hammer = WeaponObject('Hammer', 'You wield a hammer, whether a small throwing hammer, a big warhammer, or one of the squeaky toy variety.')
scyte = WeaponObject('Scythe', 'You wield a big scythe worthy of the Grim Reaper.')
kungfu = WeaponObject('Kung Fu Weapon', 'Nunchucks, Three-Section Staff, Tonfa, Sai, Tai Chi Sword, etc.')
chainsaw = WeaponObject('Chainsaw', 'Never mind how loud it is you fight with a chainsaw!')
woodenSword = WeaponObject('Wooden Sword/Staff', 'You wield bokken - Japanese-style wooden sword - or a staff.')
axe = WeaponObject('Axe/Hatchet', 'A tomahawk, battle axe, halberd, etc.')
morningStar = WeaponObject('Morningstar', 'Basically a mace with spikes. You can have a flail instead if you like.')
westerSword = WeaponObject('Western Sword', 'A long sword, rapier, flamberge, two-handed sword, etc., etc.')
whip = WeaponObject('Whip', 'A normal whip, a cat of nine tails, a metal whip, etc.')
spear = WeaponObject('Spear/Lance', 'A spear, lance, javelin, etc.')
exotic = WeaponObject('Exotic Weapon', 'A boomerang, qatar, African throwing irons, etc.')
knife = WeaponObject('Knife/Scalpel', 'You attack with a knife or scalpel. You can throw it too, and it can be a large dagger if you like.')
chainRope = WeaponObject('Chain/Rope', 'You attack with a chain or rope.')
claws = WeaponObject('Claws', 'You attack with claws, a bagh nakh, cestus, or some other claw-like weapon.')
katana = WeaponObject('Katana', 'You wield a katana, or possibly a kusarigama or some other traditional Japanese weapon.')
beamAttack = WeaponObject('Beam Attack', 'You can fire a destructive beam of light, heat, cold, or electricity from your hands or eyes. This is not a power possessed by human beings.')
fire = WeaponObject('Fire', "You can spew fire from your hands or mouth. This makes it kind of hard to believe that you're human.")
summoning = WeaponObject('Summoning', 'You are able to summon some kind of special being to attack. You can decide what you summon and how it attacks.')
magic = WeaponObject('Magic', 'You use magic to attack. Or at least something that we might as well call magic.')
psychic = WeaponObject('Psychic Powers', 'Well, you have some kind of psychic/super power that you use to attack. You can decide the details.')
book = WeaponObject('Book', 'You wield a book as a blunt instrument, and possibly tear out pages, to attack.')
internalWeap = WeaponObject('Internal Weapons', 'You have some kind of weapons installed in your body.')
religious = WeaponObject('Religious Symbol', 'You can use a cross, prayer wheel, paper charm, or other seemingly harmless religious symbol to deliver attacks.')

def returnWeaponList():
    return [
     strikingMartialArts, grapplingMartialArts, securityWeapon, tank, combatHelicopter, tortureImplements, handgun, machineGun,
     rifle, bomb, bazooka, rayGun, devilPower, hammer, scyte, kungfu, chainsaw, woodenSword, axe, morningStar, westerSword,
     whip, spear, exotic, knife, chainRope, claws, katana, beamAttack, fire, summoning, magic, psychic, book, internalWeap, religious]
