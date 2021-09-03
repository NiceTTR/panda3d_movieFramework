#import direct.directbase.DirectStart
from panda3d.core import *
from direct.interval.IntervalGlobal import *
from direct.interval.IntervalGlobal import Func, Wait, Sequence # why did the first one not work so that I have to use this one

# begin importing tew tow code

from toontown.toonbase import ToonBase
ToonBase.ToonBase()
base.initNametagGlobals()

from toontown.suit import Suit, SuitDNA
from toontown.battle import SuitBattleGlobals
from toontown.toonbase import ToontownGlobals
from panda3d.otp import CFSpeech, CFTimeout # This is very Open-Toontown specific so if you're using another source, I suggest you change panda3d.otp to the appropriate pointer.
from toontown.battle import BattleProps
from toontown.battle import BattleParticles
from toontown.toon import NPCToons, Toon, ToonDNA

from toontown.launcher.ToontownDummyLauncher import ToontownDummyLauncher
launcher = ToontownDummyLauncher()
ToonBase.launcher = launcher

# begin importing kobun42 dummy repository

try:
    from kobun42.dummy import ToontownDummyClientRepository
    base.cr = ToontownDummyClientRepository.ToontownDummyClientRepository()
except ModuleNotFoundError:
    print("The Dummy Client Repository module is missing! You may experience errors when closing or performing certain actions!")
    base.cr = None

# this allows the fucking chat noises to play
Suit.loadDialog(1)

def createSuit(cogType='f'):
    cog = Suit.Suit() # create the entity
    cog.dna = SuitDNA.SuitDNA() # make the suit actually a suit lol
    try:
        # this is actually a way to make sure the cog exists lmfao
        print("Spawning cog: " + SuitBattleGlobals.SuitAttributes[cogType]['name'] + "...")
    except:
        print("Cog type " + str(cogType) + " doesn't exist or has not been defined properly! Reverting to Flunky.")
        cogType = 'f'
    cog.dna.newSuit(cogType) # cog type thingo
    cog.setDNA(cog.dna) # set the DNA to be the cog
    try:
        cog.setName(SuitBattleGlobals.SuitAttributes[cogType]['name'])
    except:
        print("There appears to be an invalid name entry for the cog type requested. Please consider fixing that.")
        cog.setName("Suit")
    cog.nametag3d.show()
    cog.addActive()
    cog.setPickable(0)
    cog.loop('neutral')
    return cog # coggers

def createNPCToon(NPCId=2001):
    # Creates "NPC" Toons (Toons that exist as NPCs, Will make a DNA based Toon Spawner soon. Just not now.)
    try:
       print("Spawning NPC Toon: " + NPCToons.NPCToonDict[NPCId][1] + "...")
    except:
       print("NPC Toon " + str(NPCId) + " doesn't seem to exist. Did you enter the ID correctly? Reverting to Flippy.")
       NPCId = 2001
    toon = NPCToons.createLocalNPC(NPCId)
    toon.nametag3d.show()
    toon.addActive()
    toon.setPickable(0)
    toon.loop('neutral')
    return toon #TEW TOW

def createToonUsingDNA(name="Toon", head='dss', torso='ms', legs='m', gender='m', armColor=17, gloveColor=0, legColor=17, headColor=17, topTexture=3, topTextureColor=3, sleeveTexture=3, sleeveTextureColor=3, bottomTexture=7, bottomTextureColor=2):
    # Creates Regular Toons using DNA (similar to the way Player Toons are made.)
    toon = Toon.Toon()
    toonDNA = ToonDNA.ToonDNA()
    toonDNA.newToonFromProperties(head, torso, legs, gender, armColor, gloveColor, legColor, headColor, topTexture, topTextureColor, sleeveTexture, sleeveTextureColor, bottomTexture, bottomTextureColor) # UGLY HACK
    toon.setDNA(toonDNA)
    toon.setName(name)
    toon.addActive()
    toon.setPickable(0)
    toon.loop('neutral')
    return toon

def createRandomToon(name="Toon"):
    # Creates an entirely randomized toon. Results may not be the same twice. Use only if you really don't need specific character designs.
    toon = Toon.Toon()
    toonDNA = ToonDNA.ToonDNA()
    toonDNA.newToonRandom()
    toon.setDNA(toonDNA)
    toon.setName(name)
    toon.addActive()
    toon.setPickable(0)
    toon.loop('neutral')
    return toon

cog = createSuit('ym')
cog.reparentTo(render)
cog.place()
cum = Sequence()
cum.append(Wait(10))
cum.append(Func(cog.setChatAbsolute, "I deliver.", CFSpeech | CFTimeout))
cum.play()

base.oobe()
base.run()
