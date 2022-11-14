"""
Container module for the master types.
"""
from random import randint

class AgeSuperClass(object):

    def __init__(self, name='DEFAULT', descript='DEFAULT', rollText='DEFAULT'):
        self.name = name
        self.descript = descript
        self.rollText = rollText

    def generateAge(self):
        pass


class smallChild(AgeSuperClass):

    def __init__(self, name='Small Child', descript='The Master is a small child. At this age most know nothing of the outside world and have no trace of suspicion.', rollText='2D6'):
        AgeSuperClass.__init__(self, name, descript, rollText)

    def generateAge(self):
        return randint(1, 6) + randint(1, 6)


class legitimateChild(AgeSuperClass):

    def __init__(self, name='Legitimate Child', descript="The Master is still a child. He's just starting to understand his power.", rollText='5+2D6'):
        AgeSuperClass.__init__(self, name, descript, rollText)

    def generateAge(self):
        return randint(1, 6) + randint(1, 6) + 5


class layman(AgeSuperClass):

    def __init__(self, name='Layman', descript='The Master is an ordinary person who came into wealth by chance.', rollText='8+2D6'):
        AgeSuperClass.__init__(self, name, descript, rollText)

    def generateAge(self):
        return randint(1, 6) + randint(1, 6) + 8


class naturalBorn(AgeSuperClass):

    def __init__(self, name='Natural Born', descript='The Master is a young man or woman, and probably learned certain things wrong and has some twisted ideas.', rollText='12+2D6'):
        AgeSuperClass.__init__(self, name, descript, rollText)

    def generateAge(self):
        return randint(1, 6) + randint(1, 6) + 12


class aristocrat(AgeSuperClass):

    def __init__(self, name='Aristocrat', descript='This person was born to be the master of the house. Regardless of age, he has excellent self-control.', rollText='1D66'):
        AgeSuperClass.__init__(self, name, descript, rollText)

    def generateAge(self):
        return int(str(randint(1, 6)) + str(randint(1, 6)))


class recluse(AgeSuperClass):

    def __init__(self, name='Recluse', descript='The Master has already put an end to his dealings with the outside world, and adopted a secluded lifestyle.', rollText='1D66+10'):
        AgeSuperClass.__init__(self, name, descript, rollText)

    def generateAge(self):
        return int(str(randint(1, 6)) + str(randint(1, 6))) + 10


def returnMasterTypeList():
    SmallChild = smallChild()
    LegitimateChild = legitimateChild()
    Layman = layman()
    NaturalBorn = naturalBorn()
    Aristocrat = aristocrat()
    Recluse = recluse()
    return [SmallChild, LegitimateChild, Layman, NaturalBorn, Aristocrat, Recluse]
