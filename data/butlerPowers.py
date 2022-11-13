"""
Container module for the butler powers.
"""

class ButlerPowerObject(object):

    def __init__(self, name='DEFAULT', descript='DEFAULT'):
        self.name = name
        self.descript = descript


superEvasion = ButlerPowerObject('Super Evasion', 'In exchange for 1d6 Stress, you can completely avoid a single attack.')
lockPicking = ButlerPowerObject('Lock Picking', 'You can enter any room whenever you feel like. This works even when someone is using World for Two.')
stalking = ButlerPowerObject('Stalking', "When you're following someone, they won't spot you at all. (No roll possible).")
supriseAttack = ButlerPowerObject('Surprise Attack', 'In a flash you can bring out a weapon and deliver an attack. (Add +10 to the result for the first attack during combat, using a weapon).')
sawIt = ButlerPowerObject('Saw It', "You can declare that you've seen something happening in the mansion; you can decide the timing too.")
nowYouSeeHim = ButlerPowerObject('Now You See Him...', "You don't need to actually move around the mansion to get where you need to be, as you can simply appear where you like within the house.")
shadownList = [superEvasion, lockPicking, stalking, supriseAttack, sawIt, nowYouSeeHim]
support = ButlerPowerObject('Support', "By spending 1D6 Favor, you can modify someone else's die roll by +1 or -1.")
intrigue = ButlerPowerObject('Intrigue', "This butler can make rolls to resist the actions of maids, but only when the Master isn't there to see.")
knowingLaugh = ButlerPowerObject('Knowing Laugh', 'When the maids cause disruptions during your work (not including Seduction rolls), you can automatically succeed at ignoring them.')
insight = ButlerPowerObject('Insight', "With nothing more than an intent look you can make someone of the opposite sex (or maybe the same sex) feel enough feelings of love that they won't choose to attack.")
trap = ButlerPowerObject('Trap', "Even if you aren't there at the time, you can have a trap prepared in advance during a battle.")
futile = ButlerPowerObject('Futile', 'You can prevent an opponent from using any special powers or Favor points they might possess.')
eliteList = [support, intrigue, knowingLaugh, insight, trap, futile]
personInside = ButlerPowerObject('Person Inside', 'You actually have a maid inside of you somehow. You have the option of re-creating your character as a maid and participating in the game that way whenever you wish.')
fightingSpirit = ButlerPowerObject('Fighting Spirit', 'You have a powerful aura that extends for about 5 meters in every direction, and this gives you a bonus of +1 to die rolls for fighting any non-butler opponents.')
eerie = ButlerPowerObject('Eerie', 'Because of your eerie appearance and atmosphere, you can apply a -1 penalty to rolls made to resist you by members of the opposite sex.')
limiter = ButlerPowerObject('Limiter', 'Usable for attacks made using Athletics. You can make two attacks against opponents within your field of vision, but you take 10 Stress for each attack.')
giantWeapon = ButlerPowerObject('Giant Weapon', 'You can attack with a giant weapon. (+1 to Athletics for attacking).')
berserker = ButlerPowerObject('Berserker', 'When making an attack using Athletics, you can opt to an all-out attack that encompasses friends and foes alike, and adds +1 to the die roll.')
monsterList = [personInside, fightingSpirit, eerie, limiter, giantWeapon, berserker]
backup = ButlerPowerObject('Backup', 'When a maid has failed and is about to lose Favor points, you can back her up and prevent her from losing Favor.')
world4Two = ButlerPowerObject('World for Two', "By taking 1D6 Stress, you can create a 'world' for you and one other person, where for 5 minutes no one else can intrude.")
twistedLove = ButlerPowerObject('Twisted Love', 'Because of your twisted love for the Master, every time you gain Favor from the Master, you also reduce your Stress by the same amount.')
deepTrust = ButlerPowerObject('Deep Trust', 'Because of your deep bond of trust with the Master, each time you gain Favor from the Master you receive an additional 2 Favor.')
bondOfHeart = ButlerPowerObject('Bonds of the Heart', "You understand the Master's feelings better than anyone, and as such you can give him sensible assistance (+2 points of Favor gained).")
twoAsOne = ButlerPowerObject('Two As One', 'When the Master is in danger or has taken Stress, you can take the Stress yourself and instantly arrive at his location.')
partnerTable = [backup, world4Two, twistedLove, deepTrust, bondOfHeart, twoAsOne]
punishment = ButlerPowerObject('Punishment', 'When maids make mistakes, you can gain the right to punish them, without them having a chance to make an opposed roll.')
lieDetector = ButlerPowerObject('Lie Detector', "By taking 1 Stress you can make other players or the master admit if they've lied.")
oneHand = ButlerPowerObject('Old Hand', "Whether a Special Quality or a weapon, you can declare that you're conversant in skills that you haven't been shown to possess before.")
asExpected = ButlerPowerObject('As Expected', 'You can spend 2 points of Favor to automatically succeed at resisting with Luck. (Treat this as getting the same result as the opponent).')
foreboding = ButlerPowerObject('Foreboding', 'You can act as though you had knowledge of impending danger (especially Random Events) before the fact.')
consequences = ButlerPowerObject('Consequences', 'You can spend 3 Favor to re-roll the die for any action you take.')
gothicList = [punishment, lieDetector, oneHand, asExpected, foreboding, consequences]
invincible = ButlerPowerObject('Invincible', 'You take no Stress from attacks made with Attributes of 2 or less.')
crisisAdrenaline = ButlerPowerObject('Crisis Adrenaline', 'You can spend 1D6 points of Favor to add an Athletics roll to your Stress. You cannot use this to deliberately avoid the natural removal of Stress points.')
connections = ButlerPowerObject('Connections', 'You have whatever kinds of special connections you want. You can request the assistance of other groups or organizations from outside of the mansion.')
chanceMeeting = ButlerPowerObject('Chance Meeting', 'By taking 2 points of Stress, you can have an NPC who just appeared be someone you knew previously, and decide the nature of that relationship.')
manlyTears = ButlerPowerObject('Manly Tears', 'By taking 2D6 Stress, you can make requests of others (PCs or NPCs). This must be role-played.')
meatshild = ButlerPowerObject('Meatshield', "You can shield others, taking the Stress points that would've been applied to up to two others within your field of vision.")
veteranList = [invincible, crisisAdrenaline, connections, chanceMeeting, manlyTears, meatshild]

def returnButlerPowerList():
    return [
     shadownList, eliteList, monsterList, partnerTable, gothicList, veteranList]
