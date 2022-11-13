"""
Container module for master powers.
"""

class MasterPowerObject(object):

    def __init__(self, name='DEFAULT', descript='DEFAULT'):
        self.name = name
        self.descript = descript


noneMasterType = MasterPowerObject('None', "You don't seem to have any power at all. (During the game, the player can roll 2D6 and replace 'None' with some other Power Source).")
fear = MasterPowerObject('Fear', 'You are a tyrannical despot who rules by fear, or you have channels through the underworld. You have many enemies, and little time to rest easy.')
magicalPower = MasterPowerObject('Magical Power', 'Power. Magic. Something beyond the pale. You possess this, and through it your very existence demands special treatment.')
bloodTies = MasterPowerObject('Blood Ties', 'Regardless of what real power you might have, your heritage demands special treatment.')
militaryMight = MasterPowerObject('Military Might', 'You posses military might, such that no one around you would dare oppose you.')
assetsType = MasterPowerObject('Assets', "It is the fortune you've amassed that gives you your power.")
politicalPower = MasterPowerObject('Political Power', 'As the leader of an organization you have the power to command many people.')
mansion = MasterPowerObject('Mansion', 'The true value lies not in you yourself, but in the mansion where you live. Perhaps some unimaginable technology or wealth sleeps there.')
talent = MasterPowerObject('Talent', "You have a great talent in some particular area, or perhaps you're an all-around genius. Your prowess here is such that all must prostrate themselves before you.")
renown = MasterPowerObject('Renown', 'You are respected by all. You might a great hero, an enemy of all things evil.')
popularity = MasterPowerObject('Popularity', 'You have something that people find irresistible, something worthy of a king. That is why the maids serve you.')

def returnMasterPowerList():
    return [
     noneMasterType, fear, magicalPower, bloodTies, militaryMight, assetsType, politicalPower, mansion, talent, renown, popularity]
