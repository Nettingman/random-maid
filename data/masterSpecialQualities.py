"""
Container module for the master special qualities.
"""

class MasterQualityObject(object):

    def __init__(self, name='DEFAULT', descript='DEFAULT'):
        self.name = name
        self.descript = descript


glasses = MasterQualityObject('Glasses', "You wear glasses, and can't use contact lenses. The frame design can be whatever you want, and this can include a monocle.")
sickly = MasterQualityObject('Sickly', "You've got an incurable disease. However, this doesn't adversely affect your attributes.")
royalty = MasterQualityObject('Royalty', "You're among the heads of a country or organization, and as a result your life is often put in danger.")
quiet = MasterQualityObject('Quiet', "Strangely different from the 'Cool' Maid Type. No, there are no rules regarding how often you speak.")
myPace = MasterQualityObject('My Pace', "You like to live life at your own particular tempo, and you're always calm and laid-back. This does not affect your attributes.")
ocd = MasterQualityObject('OCD', "You're obsessed with hygiene management. You can't let the slighted bit of dirt pass.")
brownSkin = MasterQualityObject('Brown Skin', 'Your skin is a dark brown color, either naturally or because of tanning.')
albino = MasterQualityObject('Albino', "You have no pigment. You're not necessarily completely colorless, and this can simply be a very pale complexion.")
shy = MasterQualityObject('Shy', "You're very shy. Don't forget to remain silent when encountering NPCs you haven't met before.")
crossDresser = MasterQualityObject('Cross-Dresser', 'You outwardly appear to be of the opposite sex, which gives you a kind of perverse allure.')
imagination = MasterQualityObject('Imagination', 'You frequently get caught up in your own imaginary world.')
hermaphrodite = MasterQualityObject('Hermaphrodite', "You're both male and female. The player can decide which is the base sex.")
bishounen = MasterQualityObject('Bishounen/Bishoujo', "Not only are you attractive, but women - and men - adore you. There's a good chance that you're also romantically attracted to members of the same sex.")
nobleHair = MasterQualityObject('Noble Hair', 'Your hair is done up in long rolls, your beard is very aristocratic, or you otherwise have hair that your position amongst nobility. clear')
hedonist = MasterQualityObject('Hedonist', 'You only care about being able to passively enjoy life, or to put it nicely, you have no prejudices to speak of.')
vampire = MasterQualityObject('Vampire', 'You are a vampire, with long fangs. Be sure to act... vampiric.')
otaku = MasterQualityObject('Otaku', 'You have some obsession that you tirelessly pursue, with little or no regard for common sense.')
angel = MasterQualityObject('Angel/Devil', 'You are a being from another world charged with judging good and evil. The design and the details of your origins are up to you.')
lecherous = MasterQualityObject('Lecherous', "Sexual harassment isn't just a crime, it's a way of life.")
sadist = MasterQualityObject('Sadist', "You're excited by causing pain and suffering to others.")
masochist = MasterQualityObject('Masochist', "You're excited by being caused pain and suffering by others.")
handicapped = MasterQualityObject('Handicapped', 'You can only move around on your own with a wheelchair, or you might even outright be confined to your bed.')
scars = MasterQualityObject('Scars', 'Your face, back, etc. are covered with painful-looking scars.')
kidnapped = MasterQualityObject('Kidnapped', 'You were once kidnapped and held for 1D6 days. Even today it remains a scar in your heart.')
capableSibling = MasterQualityObject('Capable Sibling', "You have a sibling who excels at seemingly everything. You're tormented by an inferiority complex.")
familyHate = MasterQualityObject('Family Hate', 'You despise one or more of your parents or siblings. The GM can decide what if anything happened in the past.')
professionalCriminal = MasterQualityObject('Professional Criminal', "You're a professional criminal, and most of your assets no doubt came from ill-gotten gains.")
amnesiac = MasterQualityObject('Amnesiac', "You've lost your memories from when you were very young. (The GM should come up with something to reveal during the game).")
artistQuality = MasterQualityObject('Artist', 'You are a musician, painter, writer, actor, singer, composer, or some other kind of highly talented artist.')
evilEmperor = MasterQualityObject('Evil Emperor', 'You are the leader of an evil kingdom or secret society, or the leader of a group aimed at tearing down society.')
undead = MasterQualityObject('Undead', 'Despite your rotting body, you live on. This can be a mummy, zombie, lich, etc.')
scientist = MasterQualityObject('Scientist', 'You are a scientist who freely commands advanced technology, and who dabbled in countless fields.')
oracle = MasterQualityObject('Oracle', 'You can predict the future to a certain degree. There are any number of possible ways this can be carried out, and the player is free to define how their character does so.')
magician = MasterQualityObject('Magician', 'You wield sorcerous powers, in the matter of a typical fantasy wizard.')
priest = MasterQualityObject('Priest', 'You are a priest of some religion or other.')
maidQuality = MasterQualityObject('Maid Quality', "Roll 1D66 and re-roll the tens digit if it's less than 4, so you get a result from 41-66 from the Maid Special Quality table.\n>> Maid quality table")

def returnMasterQualityList():
    return [
     glasses, sickly, royalty, quiet, myPace, ocd, brownSkin, albino, shy, crossDresser, imagination, hermaphrodite, bishounen, nobleHair, hedonist, vampire, otaku, angel, lecherous, sadist, masochist, handicapped, scars, kidnapped, capableSibling, familyHate, professionalCriminal, amnesiac, artistQuality, evilEmperor, undead, scientist, oracle, magician, priest, maidQuality]
