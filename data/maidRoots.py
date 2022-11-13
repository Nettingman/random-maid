"""
Container module for maid roots.
"""

class MaidRootObject(object):

    def __init__(self, name='DEFAULT', descript='DEFAULT'):
        self.name = name
        self.descript = descript


debts = MaidRootObject('Debts', 'Your family wound up with massive debts, and you found yourself coming to work at the mansion as repayment.')
slave = MaidRootObject('Slave', 'You are a slave, and have no choice about your line of work.')
mistress = MaidRootObject('Mistress', "Although you appear to be a maid, it would be more accurate to call you the master's lover.")
revenge = MaidRootObject('Revenge', 'The master is your hated enemy, and you are infiltrating his mansion in order to extract revenge.')
orphan = MaidRootObject('Orphan', 'You are an orphan adopted by the master or his parents.')
illegitimateChild = MaidRootObject('Illegitimate Child', "You are an illegitimate child. From a legal standpoint you're no different from the master.")
hereditaryMaid = MaidRootObject('Hereditary Maid', 'You were born into a family that has served the mansion for generations.')
selfPunishment = MaidRootObject('Self Punishment', 'In order to punish yourself for your inexperience or sins, you have taken up the job of a maid.')
unrequitedLove = MaidRootObject('Unrequited Love', 'Following your one-sided love of the master, you have come here.')
business = MaidRootObject('Business', "You are a maid because you want the wages. And that's about it.")
infilitrator = MaidRootObject('Infiltrator', 'You are a member of an organization that opposes the master, and you have been sent to spy on or possibly even assassinate him.')
loyalty = MaidRootObject('Loyalty', 'You feel great loyalty to the master.')
childhoodFriendOfMaster = MaidRootObject('Childhood Friend', "As the master's childhood friend, you've used your influence to get here.")
admirerOfMaids = MaidRootObject('Admirer of Maids', "You have long admired maids, and through much hard work you've finally become one yourself.")
returningFavor = MaidRootObject('Returning a Favor', 'The master did a great service to you, and you have become a maid in order to repay him.')
distantRelative = MaidRootObject('Distant Relative', 'Although you are only distantly related to the master, your parents have put you in his care.')
bridalTraining = MaidRootObject('Bridal Training', 'You became a maid in order to prepare yourself to become an ideal bride some day.')
whoKnows = MaidRootObject('Who Knows?', "You're really not quite sure how you wound up becoming a maid.")
maidRootList = [
 debts, slave, mistress, revenge, orphan, illegitimateChild, hereditaryMaid, selfPunishment, unrequitedLove, business, infilitrator, loyalty, childhoodFriendOfMaster, admirerOfMaids, returningFavor, distantRelative, bridalTraining, whoKnows]

def returnMaidRootList():
    return maidRootList
