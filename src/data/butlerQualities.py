"""
Container module for the butler special qualities.
"""

class ButlerQualityObject(object):

    def __init__(self, name='DEFAULT', descript='DEFAULT'):
        self.name = name
        self.descript = descript


glasses = ButlerQualityObject('Glasses', "You wear glasses, and can't use contact lenses. The frame design can be whatever you want, and this can include a monocle.")
sunglasses = ButlerQualityObject('Sunglasses', "You always wear sunglasses or mirrorshades. As a rule, you don't take these off.")
furrowedBrows = ButlerQualityObject('Furrowed Brows', "Your brows are always furrowed, like you're in a bad mood.")
quiet = ButlerQualityObject('Quiet', "Strangely different from the 'Cool' Maid Type. No, there are no rules regarding how often you speak.")
myPace = ButlerQualityObject('My Pace', "You like to live life at your own particular tempo, and you're always calm and laid-back. This does not affect your attributes.")
shibui = ButlerQualityObject('Shibui', 'Most butlers are well-kept and affable gentleman. But you are beyond that. Think Sean Connery on his best days.')
brownSkin = ButlerQualityObject('Brown Skin', 'Your skin is a dark brown color, either naturally or because of tanning.')
narrowEyes = ButlerQualityObject('Narrow Eyes', "You have narrow eyes. They make it look like you're smiling. What you're really feeling is another matter entirely.")
knightTalk = ButlerQualityObject('Knight Talk', "You speak like a knight of old, saying 'thou art' and such a lot.")
dagaOnnaDa = ButlerQualityObject('A Woman', "You're actually a woman dressed as a man. Or you could be a hermaphrodite or something. You may roll for your other Special Qualities on the maids' Special Quality table if you wish.")
giant = ButlerQualityObject('Giant', "You're huge, more than two meters tall.")
muscular = ButlerQualityObject('Muscular', 'Your body is like a work of art, shrouded as it is in an armor of muscle.')
attractive = ButlerQualityObject('Attractive', 'One or more of the maids finds you attractive, if a little unapproachable because of your position.')
misshapedBody = ButlerQualityObject('Misshapen Body', 'Some part of your body has suffered damage or is otherwise abnormal. You might have one arm, a strangely bent arm, or otherwise be misshapen.')
androidQuality = ButlerQualityObject('Android', "You're not human, but rather a human-looking robot. Parts of your body are very obviously artificial.")
vampire = ButlerQualityObject('Vampire', 'You are a vampire, with long fangs. Be sure to act... vampiric.')
whiteEyes = ButlerQualityObject('White Eyes', 'Your eyes are almost completely white and have no pupils. Or, your eyes might always be glowing.')
emaciated = ButlerQualityObject('Emaciated', 'You have long, thin limbs and an emaciated body. Your figure reminds people of a spider or a wire frame.')
bishounen = ButlerQualityObject('Bishonen', "Not only are you attractive, but women - and men - adore you. There's a good chance that you're also romantically attracted to members of the same sex.")
sadist = ButlerQualityObject('Sadist', "You're excited by causing pain and suffering to others.")
sibling = ButlerQualityObject('Sibling', 'You have a relationship with one of the other Maids: You are siblings.')
sportsman = ButlerQualityObject('Sportsman', 'Pick a sport. You are a legend at playing it. The more elegant the sport, the better (fencing, polo, cricket, etc)')
patchwork = ButlerQualityObject('Patchwork', 'Your body is covered with stitching scars.')
oneEye = ButlerQualityObject('One Eye', "You have only one eye. You're free to decide whether you wear an eye patch, and if so its design.")
burns = ButlerQualityObject('Burns', 'Your face, body, etc. are covered with painful-looking scars from burns.')
masochist = ButlerQualityObject('Masochist', "You're excited by being caused pain and suffering by others.")
formetMercenary = ButlerQualityObject('Former Mercenary', "You were once a mercenary, constantly moving from battlefield to battlefield. You haven't forgotten any of your experiences or instincts from that time.")
amnesiac = ButlerQualityObject('Amnesiac', "You've lost your memories from when you were very young. (The GM should come up with something to reveal during the game).")
wanted = ButlerQualityObject('Wanted', 'The police want to question you about a serious crime. The player can decide whether the character is actually guilty.')
secretlyAssasing = ButlerQualityObject('Secretly an Assassin', "While you put on the facade of being a butler, underneath you're a coldhearted killer on the side.")
hacker = ButlerQualityObject('Hacker', "Aside from being a butler, you're a hacker, breaking into computer systems.")
doctor = ButlerQualityObject('Doctor', 'In addition to being a butler, you have the skills of a doctor or a pharmacist.')
shadowClan = ButlerQualityObject('Shadow Clan', "You're a member of one of the secret organizations that has existed throughout history. You could be a ninja, a magician, one of the knights templar, a kung fu assassin, etc.")
mummy = ButlerQualityObject('Mummy', "You're actually an animated corpse. Your complexion is bad, and you have conspicuous wounds.")
priest = ButlerQualityObject('Priest', 'You can use magic grounded in some kind of religious ceremony. You must use various types of religious symbols to do so.')
cyborg = ButlerQualityObject('Cyborg', 'You were made into a cyborg by an evil secret society or another country. You can have some special features if you wish.')

def returnButlerQualityList():
    return [
     glasses, sunglasses, furrowedBrows, quiet, myPace, shibui, brownSkin, narrowEyes, knightTalk, dagaOnnaDa,
     giant, muscular, attractive, misshapedBody, androidQuality, vampire, whiteEyes, emaciated, bishounen, sadist,
     sibling, sportsman, patchwork, oneEye, burns, masochist, formetMercenary, amnesiac, wanted, secretlyAssasing, hacker,
     doctor, shadowClan, mummy, priest, cyborg]
