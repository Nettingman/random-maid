"""
Container module for the butler types.
"""

class ButlerTypeObject(object):

    def __init__(self, name='DEFAULT', tooltip='DEFAULT', changeList=[0, 0, 0, 0, 0, 0], descript='DEFAULT'):
        self.name = name
        self.tooltip = tooltip
        self.changeList = changeList
        self.descript = descript


def returnButlerTypeList():
    shadow = ButlerTypeObject('Shadow', 'Ninja, Phantom, Escort, Surveillance Expert, Enforcer', [1, 0, 0, 0, 0, 0], 'Athletics +1')
    elite = ButlerTypeObject('Elite', 'Expert, Right-Hand Man, Trusted Friend, Cynic, Inspector, Wicked Tongue', [0, 0, 0, 1, 0, 0], 'Cunning +1')
    monster = ButlerTypeObject('Monster', 'Inhuman Strength, Unworldly, Monster, Beast', [1, 0, 0, 0, 0, 0], 'Athletics +1')
    partner = ButlerTypeObject('Partner', 'Companion, Friend, Adviser, Unbreakable Bond', [0, 1, 0, 0, 0, 0], 'Affection +1')
    gothic = ButlerTypeObject('Gothic', 'Servant, Austere, Mechanical, Educator, Manager', [0, 0, 1, 0, 0, 0], 'Skill +1')
    veteran = ButlerTypeObject('Veteran', 'Expert, Old Hand, Coach, All-Purpose', [0, 0, 0, 0, 0, 0], 'Any One Attribute +1\n(Raise this attribute manually!)')
    return [shadow, elite, monster, partner, gothic, veteran]
