"""
Container module for the maid powers.
"""

class MaidPowerObject(object):

    def __init__(self, name='DEFAULT', descript='DEFAULT', stat='DEFAULT'):
        self.name = name
        self.descript = descript
        self.stat = stat


superEvasion = MaidPowerObject('Super Evasion', 'In exchange for 1d6 Stress, you can completely avoid a single attack.', 'ATH')
ironWall = MaidPowerObject('Iron Wall', 'You can use your Athletics attribute to defend up to two other characters.', 'ATH')
trespass = MaidPowerObject('Trespass', 'You can take 1d6 Stress to intrude on a battle, love scene, etc. You can also butt in after the action has ended, and this can even work when someone is using World For Two.', 'ATH')
weaponFromNowhere = MaidPowerObject('Weapon From Nowhere', 'You can pull your weapon out seemingly from nowhere, and get in a surprise attack. If you make a surprise attack, you get to make an attack roll without the target getting to make an opposed roll.', 'ATH')
giantWeapon = MaidPowerObject('Giant Weapon', 'You can attack with a giant weapon. (+1 to Athletics for attacking).', 'ATH')
ultimateRetort = MaidPowerObject('Ultimate Retort', 'You can blow off an opponent completely by delivering a good retort (GM decides). You can make it impossible to defend against this by taking 2 Stress. (This must be role-played).', 'ATH')
ATHList = [superEvasion, ironWall, trespass, weaponFromNowhere, giantWeapon, ultimateRetort]
maidensTears = MaidPowerObject("Maiden's Tears", "By taking 2D6 Stress, you can make a request that can't be refused. (This must be role-played).", 'AFF')
world4Two = MaidPowerObject('World for Two', "By taking 1D6 Stress, you can create a 'world' for you and one other person, where for 5 minutes no one else can intrude", 'AFF')
powerOfFriendship = MaidPowerObject('Power of Friendship', 'You can take 1D6 Stress in order to remove 2D6 Stress from someone else.', 'AFF')
cookedWithLove = MaidPowerObject('Cooked With Love', "When someone eats food you've prepared, they lose 1D6 Stress.", 'AFF')
windowsOfSoul = MaidPowerObject('Windows of the Soul', "You understand the master's feelings better than anyone, and can offer careful help. (Add 2 to Favor gained).", 'AFF')
passionateGaze = MaidPowerObject('Passionate Gaze', 'With just a glance, you can ingratiate yourself with the master, taking 1D6 Stress to gain 1D3 Favor.', 'AFF')
AFFList = [maidensTears, world4Two, powerOfFriendship, cookedWithLove, windowsOfSoul, passionateGaze]
lockPicking = MaidPowerObject('Lock Picking', 'You can enter any room whenever you feel like. This works even when someone is using World for Two.', 'SKI')
stalking = MaidPowerObject('Stalking', "When you're following someone, there's no chance for them to detect you. Don't even bother rolling dice.", 'SKI')
lieDetector = MaidPowerObject('Lie Detector', "By taking 1 Stress you can make other players or the master admit if they've lied.", 'SKI')
ultimateMenu = MaidPowerObject('Ultimate Menu', 'Add +1 to your Skill for the purposes of cooking.', 'SKI')
instantCleaning = MaidPowerObject('Instant Cleaning', 'Add +1 to your Skill for the purposes of doing cleaning.', 'SKI')
fourDDress = MaidPowerObject('4-D Dress', 'You can produce anything in the mansion from within your maid uniform.', 'SKI')
SKIList = [lockPicking, stalking, lieDetector, ultimateMenu, instantCleaning, fourDDress]
punishment = MaidPowerObject('Punishment', 'When other maids make mistakes, you can gain the right to punish them, without them having a chance to make an opposed roll.', 'CNN')
instantRestrain = MaidPowerObject('Instant Restraint', 'If you win a roll of Cunning Vs. Athletics, you can restrain someone from doing something indecent.', 'CNN')
coercion = MaidPowerObject('Coercion', "If you win a roll of Cunning Vs. Athletics, you can completely damage or tear off someone's clothes, even 'accidentally'.", 'CNN')
trap = MaidPowerObject('Trap', "Even if you aren't there at the time, you can have a trap prepared in advance during a battle.", 'CNN')
fakeCrying = MaidPowerObject('Fake Crying', 'You can use fake frying to use your Cunning for what would normally be an Affection roll. (This must be role-played).', 'CNN')
mockery = MaidPowerObject('Mockery', 'When someone is taking Stress points, you can mock them and cause them to gain an additional 2 Stress points. (This must be roleplayed).', 'CNN')
CNNList = [punishment, instantRestrain, coercion, trap, fakeCrying, mockery]
karma = MaidPowerObject('Karma', 'You can use your Luck to dodge an attack, and if you roll a 10 or higher you cause twice as much Stress to the opponent.', 'LCK')
sawIt = MaidPowerObject('Saw It', "You can declare that you've seen something happening in the mansion; you can decide the timing too.", 'LCK')
teleport = MaidPowerObject('Teleport', 'You can go just about anywhere in the mansion instantly.', 'LCK')
escape = MaidPowerObject('Escape', 'You can completely flee from a battle without taking any Stress.', 'LCK')
foreboding = MaidPowerObject('Foreboding', 'You can tell when something dangerous is coming.', 'LCK')
chanceMeeting = MaidPowerObject('Chance Meeting', "By taking 2 points of Stress, you can have an NPC that's just showing up for the first time be an acquaintance from some time before.", 'LCK')
LCKList = [karma, sawIt, teleport, escape, foreboding, chanceMeeting]
immune2Pain = MaidPowerObject('Immune to Pain', "During a battle, even if you're sent flying, you don't take any Stress. Outside of battle, however, you can still take Stress points like usual.", 'WIL')
crisisAdrenaline = MaidPowerObject('Crisis Adrenaline', 'You can spend 1D6 points of Favor to add an Athletics roll to your Stress. You cannot use this to deliberately avoid the natural removal of Stress points.', 'WIL')
persistence = MaidPowerObject('Persistence', 'Whenever you take Stress, automatically reduce the amount by 1', 'WIL')
tenacity = MaidPowerObject('Tenacity', 'Even after being defeated in battle, you can take 2 Stress to get to your feet.', 'WIL')
hardWork = MaidPowerObject('Hard Work', 'Your relentless hard work pays off in the form of a +3 bonus to the end result (not the attribute or die roll) of Skill rolls.', 'WIL')
absoluteMaid = MaidPowerObject('Absolute Maid', 'You are the very epitome of a maid, and you take no penalties when not in full uniform.', 'WIL')
WILList = [immune2Pain, crisisAdrenaline, persistence, tenacity, hardWork, absoluteMaid]
maidPowerList = [
 ATHList, AFFList, SKIList, CNNList, LCKList, WILList]

def returnMaidPowerList():
    return maidPowerList
