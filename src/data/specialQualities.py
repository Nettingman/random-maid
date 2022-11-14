"""
Container module for the special qualities.
"""

class SecondaryTableObject(object):

    def __init__(self, name='DEFAULT', descript='DEFAULT'):
        self.name = name
        self.descript = descript


tights = SecondaryTableObject('Tights', "In place of a skirt, you wear tights of some color. Athletic, colorful, sexy, or weird (leopard pattern, RAWR!) it's up to you. (For the purposes of the maid uniform rules, treat these as a skirt)")
chinaDress = SecondaryTableObject('China Dress', 'You wear a Chinese-style cheongsam maid uniform. (For the purposes of the rules, treat this as a one-piece maid uniform).')
armor = SecondaryTableObject('Armor', 'Your maid uniform is actually a stylized suit of metal armor.')
bondage = SecondaryTableObject('Bondage', 'Your maid uniform is made of shiny rubber or leather, and generally a bit suspicious.')
miniskirt = SecondaryTableObject('Miniskirt', 'Your skirt is very short, to the point where one can almost see its contents.')
kappougi = SecondaryTableObject('Kappougi', 'Instead of a Western maid uniform, you wear a Japanese-style one with a kimono and an apron over it.')
uniformTable = [tights, chinaDress, armor, bondage, miniskirt, kappougi]
skull = SecondaryTableObject('Skull', 'Your headdress, apron, necktie, forehead, or chest has a skull mark.')
bat = SecondaryTableObject('Bat', 'Your headdress, apron, necktie, forehead, or chest has a bat symbol.')
crossSymbol = SecondaryTableObject('Cross', 'Your headdress, apron, necktie, forehead, or chest has a cross on it.')
yinyang = SecondaryTableObject('Yin-Yang', 'Your headdress, apron, necktie, forehead, or chest has a yin-yang symbol.')
starSymbol = SecondaryTableObject('Star', 'Your headdress, apron, necktie, forehead, or chest has a yin-yang symbol.')
cardSuit = SecondaryTableObject('Card suit', 'Your headdress, apron, necktie, forehead, or chest has a yin-yang symbol.')
symbolTable = [skull, bat, crossSymbol, yinyang, starSymbol, cardSuit]
cigarettes = SecondaryTableObject('Cigarettes', "You've always got a cigarette in your mouth, or are chomping on a cigar.")
tattoo = SecondaryTableObject('Tattoo', 'Somewhere on your body - or maybe even all over it - you have a tattoo.')
sunglasses = SecondaryTableObject('Sunglasses', 'You always wear sunglasses or mirrorshades. Even at night.')
badExpression = SecondaryTableObject('Bad Expression', "You have a perpetual unpleasant facial expression (as if you're always angry, or always about to kick ass at any moment), and this makes first meetings difficult.")
piercing = SecondaryTableObject('Piercings', 'You have piercings, and not just in your ears, but perhaps your forehead, lips, eyelids, chin, etc.')
roughSpeak = SecondaryTableObject('Rough Speak', 'You talk like a gangster, be it a Mafioso or a street ganger.')
delinquentTable = [cigarettes, tattoo, sunglasses, badExpression, piercing, roughSpeak]
southAccent = SecondaryTableObject('Southern', "Y'all talk like some kinda' country bumpkin or somethin', from down in the American South.")
brithishAccent = SecondaryTableObject('British', "You talk with a British accent of some kind. We'll leave it up to you what kind specifically. If you are already from the UK in real life, then you are now DOUBLE BRITISH. Or choose Scottish or Welsh.")
pidginEnglish = SecondaryTableObject('Pidgin English', "You come from a country/society where English is taught as a pidgin language. You might sound like a Japanese salaryman or pop idol ('Body Feels Exit!'). Pick a country and go with it.")
meow = SecondaryTableObject('Meow', 'You like to sprinkle cat sounds in your speech every now and then.')
knight = SecondaryTableObject('Knight', "You sound like a knight from a movie, or possibly a Renaissance Faire reject. Remember to say 'Thou art' and whatnot a lot.")
foreigner = SecondaryTableObject('Foreigner', 'Pick a foreign nationality for your Maid other than Japanese. American (Brooklyn, Texas), French, Russian, Mexican, Nigerian, Indian, Canadian, etc.')
accentTable = [southAccent, brithishAccent, pidginEnglish, meow, knight, foreigner]
longRinglets = SecondaryTableObject('Long Ringlets', 'Your hair is done up in large, long ringlets.')
dumplings = SecondaryTableObject('Dumplings', "Your hair is long, with 'dumplings' on top.")
mesh = SecondaryTableObject('Mesh', "You have a mesh haircut, a short, stylish hairdo that's trendy in Japan.")
curlyHair = SecondaryTableObject('Curly Hair', 'Your hair is curly enough to defy gravity, and always takes the same shape.')
oneEyeHair = SecondaryTableObject('One Eye Hair', 'Your hair hangs down so that it conceals one of your eyes.')
antennaHair = SecondaryTableObject('Antenna Hair', 'Your hair has antennas/feelers and a mind of its own.')
hairTable = [longRinglets, dumplings, mesh, curlyHair, oneEyeHair, antennaHair]
collar = SecondaryTableObject('Collar', 'Your hair has antennas/feelers and a mind of its own.')
largeRibbon = SecondaryTableObject('Large Ribbon', 'You wear a large ribbon in your hair.')
spike = SecondaryTableObject('Spike', 'Your maid uniform has spikes attached to it.')
chains = SecondaryTableObject('Chains', 'Your maid uniform has jangling chains attached to it.')
blackLeatherGloves = SecondaryTableObject('Black Leather Gloves', 'You normally wear black leather gloves. These can be fingerless or have rivets if you like.')
pet = SecondaryTableObject('Pet', 'You have a cat, snake, raven, or some other small animal as a pet that rests on your shoulder or in your hand.')
accessoryTable = [collar, largeRibbon, spike, chains, blackLeatherGloves, pet]
sibling = SecondaryTableObject('Sibling or Nymphomaniac', "You're related by blood to one of the other characters.\nor\nYou're abnormally interested in physical love. It's up to the players and GM to decide how far you want to, or should, roleplay this.")
childhoodFriend = SecondaryTableObject('Childhood Friends or Sadist', "You grew up together in the same neighborhood as one of the other characters, and have been great friends since a very early age.\nor\nYou're excited by causing pain and suffering to others.")
mentor = SecondaryTableObject('Mentor or Masochist', "You look upon one of the characters as a personal mentor, perhaps even as a father/mother figure\nor\nYou're excited by being caused pain and suffering by others.")
rival = SecondaryTableObject('Friendly Rival or Womanizer', "You and another character are rivals in some area of life, and you always find yourself both consciously or subconsciously competing with, and comparing yourself with, that person. However, you are still friends (at least in appearance).\nor\nYou're only romantically attracted to members of the same sex, which is fine (and perhaps expected)... But in your case, it's turned up to '11'.")
exlover = SecondaryTableObject('Ex-Lover/Love Rival or Likes Them Young', "You used to date another character. Perhaps there are still feelings. Alternately, you both might be seeking the love of a third person.\nor\nYou're only interested in . . . younger partners. You can decide what age range this entails.")
vengeance = SecondaryTableObject('Vengeance or Exhibitionist', "Another character wronged you in some way in the past. She may not even realize that she did (and it might not have seemed a big deal). But you will never forget.\nor\nYou enjoy showing off your nude or semi/nude body. 'Inappropriate dress' is not just a word, it's a way of life.")
relationShipTable = [sibling, childhoodFriend, mentor, rival, exlover, vengeance]
killer = SecondaryTableObject('Killer', 'You have a bad habit: killing people.')
pyro = SecondaryTableObject('Pyromaniac', 'You love setting fires. You might even set fire to the mansion . . .')
klepto = SecondaryTableObject('Kleptomaniac', "You can't help but steal things, regardless of whether or not you have any use for them.")
addict = SecondaryTableObject('Addict', "Whether it's narcotics, stimulants, or just sleeping pills, you're a substance-abuser. If you don't get to have any, you'll experience withdrawal symptoms.")
otaku = SecondaryTableObject('Otaku', 'You have some obsession that you tirelessly pursue, with little or no regard for common sense.')
stalker = SecondaryTableObject('Stalker', "You're stalking a particular person. Select the target from among the other PCs or the master.")
criminalTendencyTable = [killer, pyro, klepto, addict, otaku, stalker]
patchwork = SecondaryTableObject('Patchwork', 'Your body is covered with stitching scars.')
oneEye = SecondaryTableObject('One Eye', "You have only one eye. You're free to decide whether you wear an eye patch, and if so its design.")
burns = SecondaryTableObject('Burns', 'Your face, body, etc. are covered with painful-looking scars from burns.')
whipScars = SecondaryTableObject('Whip Scars', 'Your back and such is covered with painful-looking welts from whippings you received (and may possibly be still receiving?)')
bandages = SecondaryTableObject('Bandages', 'You wear many bandages and casts, concealing injuries that will not heal.')
blind = SecondaryTableObject('Blind', 'You were rendered blind a long time ago. (No particular penalties for this: See the classic Zatoichi movies for reference).')
injuryTable = [patchwork, oneEye, burns, whipScars, bandages, blind]
separation = SecondaryTableObject('Separations', "For some reason love just never works out for you. At this point you've resigned yourself to fate.")
loverDied = SecondaryTableObject('Lover Died', "You had a lover who died since then you've been afraid to fall in love.")
killedYourLover = SecondaryTableObject('Killed Your Lover', "For whatever reason, you killed your last lover since then you've been afraid to fall in love. Or afraid for the object of your desire.")
formerProst = SecondaryTableObject('Former Prostitute', 'You used to sell your body, for cheap. A complex remains.')
betrayal = SecondaryTableObject('Betrayal', "You were once betrayed by a lover since then you've been afraid to fall in love or let your guard down.")
stalkerDamage = SecondaryTableObject('Stalker Damage', "You were once victimized by a stalker. You can't trust members of the opposite sex . . . or maybe the same sex.")
tragicLoveTable = [separation, loverDied, killedYourLover, formerProst, betrayal, stalkerDamage]
formerDelinq = SecondaryTableObject('Former Delinquent', "Although no one would know it looking at you now, you used to be a delinquent. Fortunately right now there's no one (in the mansion at least) who knows about your past.")
formerKiller = SecondaryTableObject('Former Killer', 'You were once a hired killer. Even now, your skills have not been dulled.')
amnesiac = SecondaryTableObject('Amnesiac', "You've lost your memories from when you were very young. (The GM should come up with something to reveal during the game).")
badReputation = SecondaryTableObject('Bad Reputation', 'You were involved with some bad stuff back in the day, and you have the dubious honor of being a legend for all the wrong reasons.')
wanted = SecondaryTableObject('Wanted', 'The police want to question you about a serious crime. The player can decide whether or not the character is actually guilty.')
runaway = SecondaryTableObject('Runaway', "You've left your real home without permission.")
darkPastTable = [formerDelinq, formerKiller, amnesiac, badReputation, wanted, runaway]
suicideAttempts = SecondaryTableObject('Suicide Attempts', 'In the past, you attempted suicide many times.')
killedYourParents = SecondaryTableObject('Killed Your Parents', 'For whatever reason, you are responsible for the death of your parents.')
sawParentDie = SecondaryTableObject('Saw Parent Die', "You witnessed your parents' (one or both) death with your own eyes.")
siblingHate = SecondaryTableObject('Sibling Hate', 'You and your sister(s) detest each other.')
familyBreakup = SecondaryTableObject('Family Breakup', 'For some reason (economic trouble?) your family was forced to break up. You may have even caused it.')
abusiveParent = SecondaryTableObject('Abusive Parents', 'You were raised by abusive parents.')
traumaTable = [suicideAttempts, killedYourParents, sawParentDie, siblingHate, familyBreakup, abusiveParent]
assassin = SecondaryTableObject('Assassin', "While you put on the facade of being a maid, underneath you're a coldhearted killer for hire.")
hacker = SecondaryTableObject('Hacker', "Aside from being a maid, you're a hacker, breaking into computer systems.")
scientist = SecondaryTableObject('Scientist', "Along with being a maid, you're some kind of mad scientist.")
doctor = SecondaryTableObject('Doctor/Pharmacist', 'In addition to being a maid, you have the skills of a doctor or a pharmacist.')
doujinArtist = SecondaryTableObject('Doujin Artist', 'In addition to being a maid, you create doujinshi in your spare time. You can decide the genre.')
proCreator = SecondaryTableObject('Pro Creator', "Along with being a maid, you're working as a professional creator, craftsperson or artist. You can decide the form and genre of your works.")
secretJobTable = [assassin, hacker, scientist, doctor, doujinArtist, proCreator]
evilSecretSociety = SecondaryTableObject('Evil Secret Society', "You're a member of an evil secret society that seeks to conquer or destroy the world.")
secretAgency = SecondaryTableObject('Secret Agency', "You're part of a secret agency under the government or the United Nations, some sort of intelligence agent or spy.")
cult = SecondaryTableObject('Cult', "You're a member of some kind of eccentric cult, whether as a believer, a leader, or even the founder.")
politicalOrg = SecondaryTableObject('Political Organization', "You're part of a group organized around some kind of political ideal, possibly something extreme to the point of insanity.")
shadowClan = SecondaryTableObject('Shadow Clan', "You're a member of one of the secret organizations that has existed throughout history. You could be a ninja, a magician, one of the knights templar, a kung fu assassin, etc.")
governmentOfficial = SecondaryTableObject('Government Official', "You're actually a government official who is working as a maid, whether because you're a nurse, a detective going undercover, or a politician's secretary.")
memberShipTable = [evilSecretSociety, secretAgency, cult, politicalOrg, shadowClan, governmentOfficial]
fox = SecondaryTableObject('Fox', "You're actually a fox, and can display or hide your ears and tail at will.")
spider = SecondaryTableObject('Spider', "You're actually a spider, and you can become an actual human-sized spider, or else just grow up to six extra arms at will.")
raven = SecondaryTableObject('Raven', "You're actually a raven. You have black wings that can be displayed or hidden.")
bunny = SecondaryTableObject('Bunny', "You're actually a bunny, with bunny ears and a tail.")
tiger = SecondaryTableObject('Tiger/Lion', "You're actually a predatory cat, and you have ears, a tail, claws, and sharp teeth than you can display or hide at will.")
snake = SecondaryTableObject('Snake', "You're actually a snake, and you can take on a naga form, turning the lower half of your body into a snake tail.")
shapeShifterTable = [fox, spider, raven, bunny, tiger, snake]
mermaid = SecondaryTableObject('Mermaid', "You're actually a mermaid. You love water, and your ears sometimes look like fins.")
zombie = SecondaryTableObject('Zombie/Mummy', "You're actually an animated corpse. Your complexion is probably bad, and you have conspicuous wounds.")
werewolf = SecondaryTableObject('Werewolf', "You're actually a werewolf (or maybe a weretiger). Whether or not you want to, you turn into a wolf (or tiger) during a full moon.")
succubus = SecondaryTableObject('Succubus', "You're actually a succubus, a female demon that traps her prey by arousing their desires. You have some demonic physical traits (you decide the specifics) that can be displayed or hidden.")
ghost = SecondaryTableObject('Ghost', "You're actually a ghost. You might have been one of the master's ancestors, or perhaps a maid who worked at the mansion in the past.")
shinigami = SecondaryTableObject('Shinigami', "You're actually a shinigami, a death reaper. As such, you carry with you an aura of death. You might be there to deliver a specific person to the other side, or perhaps your reasons are more mundane.")
monsterTable = [mermaid, zombie, werewolf, succubus, ghost, shinigami]
pristess = SecondaryTableObject('Priestess', 'You can use magic grounded in some kind of religious ceremony. You must use various types of religious symbols to do so.')
onmyouji = SecondaryTableObject('Onmyouji', 'You practice Eastern-style magic based on Taoist principles. Your key item for this is jufu, special curse charms written in brush ink on strips of paper.')
fortuneteller = SecondaryTableObject('Fortuneteller', 'Within certain limits, you have the ability to predict the future. There are countless methods of divination.')
westerMagician = SecondaryTableObject('Western Magician', 'You practice alchemy, Kabbalah, or some other form of Western sorcery. As such, you are a staffwielding orthodox magician.')
devilSummoner = SecondaryTableObject('Devil Summoner', 'You know the spells necessary to summon demons. Your tools of the trade are magic circles, a black cloak, and ancient books.')
necromancer = SecondaryTableObject('Necromancer', 'You wield magic that lets you control the souls and bodies of the dead. Your tools of the trade include skulls and black clothes.')
magicTable = [pristess, onmyouji, fortuneteller, westerMagician, devilSummoner, necromancer]
alien = SecondaryTableObject('Alien', "You're an alien who came to our world from somewhere in outer space. Your body can have some special properties if you wish.")
cyborg = SecondaryTableObject('Cyborg', 'You were turned into a cyborg by an evil secret society or some other country. Your body can have some special features if you wish.')
runawayNinja = SecondaryTableObject('Runaway Ninja', 'You ran away from your ninja village.')
magicalGirl = SecondaryTableObject('Magical Girl', 'You came from a land of magic in order to train.')
fairy = SecondaryTableObject('Fairy', "You're one of the fae folk. You can be a generic pixie, or something more specific.")
mutant = SecondaryTableObject('Mutant', "You've suffered some kind of strange mutation.")
absurdTable = [alien, cyborg, runawayNinja, magicalGirl, fairy, mutant]

class PrimaryTableObject(object):

    def __init__(self, name, descript, secondaryTable=[]):
        self.name = name
        self.descript = descript
        self.secondaryTable = secondaryTable


glasses = PrimaryTableObject('Glasses', "You wear glasses, and can't use contact lenses. The frame design can be whatever you want.")
freckles = PrimaryTableObject('Freckles', 'You have freckles.')
sickly = PrimaryTableObject('Sickly', "You've got an incurable disease. However, this doesn't adversely affect your attributes. Choose your own symptoms.")
quiet = PrimaryTableObject('Quiet', 'You have a cool, subtle demeanor. No, there are no rules regarding how often you speak.')
easygoing = PrimaryTableObject('Easygoing', "You take things slow and calm, at your own pace. This doesn't affect your attributes.")
neatFreak = PrimaryTableObject('Neat Freak', "You're obsessed with cleanliness, and can't let the tiniest bit of dirt go unnoticed.")
brownSkin = PrimaryTableObject('Brown Skin', 'Your skin is a dark brown color. It could be natural, or a tan.')
albino = PrimaryTableObject('Albino', "You have no pigment. You're not necessarily completely colorless, this could simply be a very pale complexion.")
shy = PrimaryTableObject('Shy', "You're very shy. Don't forget to remain silent when encountering NPCs you haven't met before.")
dagaOtokoDa = PrimaryTableObject('Actually A Guy', "You're actually a guy (cross-dresser?). Or possibly a hermaphrodite.")
overactiveImagiantion = PrimaryTableObject('Overactive Imagination', 'You frequently get caught up in your own imaginary world, or else tend to daydream a lot.')
greedy = PrimaryTableObject('Greedy', 'You will do absolutely anything for the sake of money.')
elfEars = PrimaryTableObject('Elf Ears', 'You have long, pointed ears.')
nekomimi = PrimaryTableObject('Nekomimi', "This varies a bit depending on the setting, but you're a catgirl, with the ears and possibly tail of a cat.")
android = PrimaryTableObject('Android/Gynoid', "You're not human, but rather a human-looking robot. Parts of your body are very obviously artificial.")
vampire = PrimaryTableObject('Vampire', 'You are a vampire, with long fangs. Be sure to act . . . vampiric.')
princess = PrimaryTableObject('Princess', "You're actually the daughter of a family of even greater standing than the master. Depending on the setting, you could even be from another country's royal family. Whether you are in disguise or not is up to you.")
angel = PrimaryTableObject('Angel/Devil', 'You are a being from another world charged with judging good and evil. The design and the details of your origins are up to you.')
uniform = PrimaryTableObject('Uniform', "You've managed to make a special arrangement with your uniform.\n>> Uniform table", uniformTable)
symbolQuality = PrimaryTableObject('Symbol', 'You have some kind of special mark on your uniform of headdress.\n>> Symbol table', symbolTable)
delinquent = PrimaryTableObject('Delinquent', 'Something about you is very much like a delinquent.\n>> Delinquent table', delinquentTable)
accentQuality = PrimaryTableObject('Accent', 'You have an unusual way of speaking.\n>> Accent table', accentTable)
hairStyle = PrimaryTableObject('Hairstyle', 'You have a special hairstyle.\n>> Hairstyle table', hairTable)
accessory = PrimaryTableObject('Accessory', 'You have a special accessory attached to your uniform.\n>> Accessory table', accessoryTable)
relationShip = PrimaryTableObject('Relationship or Perversion', 'Lighter Game? You have a relationship to another player character (Maid).\n>> Relationship table\nDarker Game? You have a bizarre perversion of some kind.\n>> Perversion table', relationShipTable)
criminalTendency = PrimaryTableObject('Criminal Tendencies', 'You have an inclination towards criminal acts.', criminalTendencyTable)
injury = PrimaryTableObject('Injury', 'Because of mistreatment or an accident, you have some kind of permanent physical injury.\n>> Injury table', injuryTable)
tragicLove = PrimaryTableObject('Tragic Love', 'You have had sad or tragic experiences with love.\n>> Tragic love table', tragicLoveTable)
darkPast = PrimaryTableObject('Dark Past', 'There is something dark in your personal history.\n>> Dark past table', darkPastTable)
trauma = PrimaryTableObject('Trauma', 'After some terrible incident, you were traumatized.\n>> Trauma table', traumaTable)
secretJob = PrimaryTableObject('Secret Job', "You're not just a maid: you're secretly holding another job.\n>> Secret job table", secretJobTable)
memberShip = PrimaryTableObject('Membership', "In addition to being a maid, you're also a member of a certain organization.\n>> Membership table", memberShipTable)
shapeShifter = PrimaryTableObject('Shapeshifter', 'You are an animal or weapon that has taken the form of a maid.\n>> Shapeshifter table', shapeShifterTable)
monster = PrimaryTableObject('Monster', "You're not human, but rather some kind of monster.\n>> Monster table", monsterTable)
magic = PrimaryTableObject('Magic', 'You can use some kind of magical power.\n>> Magic table', magicTable)
absurd = PrimaryTableObject('Absurd', "You're something that flies in the face of common sense.\n>> Absurd table", absurdTable)
specialQualityTable = [
 glasses, freckles, sickly, quiet, easygoing, neatFreak, brownSkin, albino, shy, dagaOtokoDa, overactiveImagiantion, greedy, elfEars, nekomimi, android, vampire, princess, angel, uniform, symbolQuality, delinquent, accentQuality, hairStyle, accessory, relationShip, criminalTendency, injury, tragicLove, darkPast, trauma, secretJob, memberShip, shapeShifter, monster, magic, absurd]

def returnSpecialQualityList():
    return specialQualityTable
