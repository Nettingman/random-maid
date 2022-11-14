"""
Container module for the stress explosions.
"""

class StressExplosionObject(object):

    def __init__(self, name='DEFAULT', descript='DEFAULT'):
        self.name = name
        self.descript = descript


alcohol = StressExplosionObject('Alcohol/Drugs', "You drink alcohol (or drugs) until you can't remember or care.")
stealing = StressExplosionObject('Stealing', 'You steal valuables from the mansion or from other maids.')
violence = StressExplosionObject('Violence', 'You unleash violence on the other maids and the master.')
gambling = StressExplosionObject('Gambling', 'You use every penny you have for gambling.')
racing = StressExplosionObject('Racing', 'You get into whatever car/vehicle is handy and go for a drive at at least twice the speed limit.')
teasing = StressExplosionObject('Teasing', 'You start persistently tormenting the other maids.')
mischief = StressExplosionObject('Mischief', 'You start playing troublesome tricks on the master and the other maids.')
runningAway = StressExplosionObject('Running Away', 'You run away from the mansion.')
complaining = StressExplosionObject('Complaining', 'You start incessantly complaining to the master and other maids.')
seclusion = StressExplosionObject('Seclusion', "You go into your room and won't come out, not even for food.")
crying = StressExplosionObject('Crying', "You start crying. There's no need for an Affection check for this.")
rampage = StressExplosionObject('Rampage', 'You use anything you can lay your hands on to run around destroying things around the mansion.')
shopping = StressExplosionObject('Shopping', 'You go crazy spending your money on shopping.')
sleep = StressExplosionObject('Sleep', 'You spend all day sleeping.')
binge = StressExplosionObject('Binge', 'You go crazy eating.')
prayer = StressExplosionObject('Prayer', 'You escape through religion, relentlessly praying to heaven for protection.')
spoiledChild = StressExplosionObject('Spoiled Child', 'You act like a spoiled child, making demands of the master.')
playerChoice = StressExplosionObject('Player Choice', 'Let the player to your left decide for you.')
stressExplosionList = [
 alcohol, stealing, violence, gambling, racing, teasing, mischief, runningAway, complaining, seclusion, crying, rampage, shopping, sleep, binge, prayer, spoiledChild, playerChoice]

def returnStressExplosionList():
    return stressExplosionList
