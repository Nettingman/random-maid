"""
Container module for the maid types.
"""

class MaidTypeObject(object):

    def __init__(self, name='DEFAULT', tooltip='DEFAULT', changeList=[0, 0, 0, 0, 0, 0], descript='DEFAULT'):
        self.name = name
        self.tooltip = tooltip
        self.changeList = changeList
        self.descript = descript


def returnMaidTypeList():
    lolita = MaidTypeObject('Lolita', 'Childish, young, innocent, cute, sweet.', [-1, 0, 0, 0, 1, 0], 'Luck +1, Athletics -1')
    sexy = MaidTypeObject('Sexy', 'Charming, coquettish, womanly body, glamorous.', [0, 0, 0, 1, 0, -1], 'Cunning +1, Will -1')
    pure = MaidTypeObject('Pure', 'Pure, maidenly, clean, fragile.', [0, 1, 0, -1, 0, 0], 'Affection +1, Cunning -1')
    cool = MaidTypeObject('Cool', 'Composed, expressionless, unflappable, doll-like.', [0, -1, 1, 0, 0, 0], 'Skill +1, Affection -1')
    boyish = MaidTypeObject('Boyish', 'Wild, energetic, vigorous, at first glance looks like a boy.', [1, 0, -1, 0, 0, 0], 'Athletics +1, Skill -1')
    heroine = MaidTypeObject('Heroine', 'Earnest, single-minded, tries her very best.', [0, 0, 0, 0, -1, 1], 'Will +1, Luck -1')
    retList = [
     lolita, sexy, pure, cool, boyish, heroine]
    return retList
