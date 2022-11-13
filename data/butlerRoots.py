"""
Container module for butler roots.
"""

class ButlerRootObject(object):

    def __init__(self, name='DEFAULT', descript='DEFAULT'):
        self.name = name
        self.descript = descript


hatred = ButlerRootObject('Hatred', 'His dark hatred will not be satisfied by mere violence, and he lies in wait to bring true despair to bear.')
ambition = ButlerRootObject('Ambition', "His desire stirs him. He conceals your sharp fangs beneath a mask of subservience, until the day when he's ready to take everything that belongs to the Master.")
contract = ButlerRootObject('Contract', "He works in the mansion simply as part of a clear-cut employment contract. At the very least, the pay isn't bad.")
affection = ButlerRootObject('Affection', "He feels deep affection for the Master, the maids, and even the mansion itself. He sees them as difficult children he loves so much he can't help but tend to them.")
loyalty = ButlerRootObject('Loyalty', 'He serves the mansion as a shield, and his loyalty is absolute. He will do anything for the master of the house, even at the cost of his own life.')
family = ButlerRootObject('Family', "He can be thought of as the Master's family. They both need each other, and the division between Master and servant is not so obvious.")

def returnButlerRootList():
    return [
     hatred, ambition, contract, affection, loyalty, family]
