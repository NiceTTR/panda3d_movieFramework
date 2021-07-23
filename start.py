#import direct.directbase.DirectStart
from panda3d.core import *
#from direct.gui.OnscreenText import OnscreenText
#from direct.actor.Actor import Actor
#from direct.showbase.DirectObject import DirectObject
from direct.interval.IntervalGlobal import *
from direct.interval.IntervalGlobal import Func, Wait, Sequence # why did the first one not work so that I have to use this one

# begin importing tew tow code

from toontown.toonbase import ToonBase
ToonBase.ToonBase()
base.initNametagGlobals()

from toontown.suit import Suit, SuitDNA
from toontown.battle import SuitBattleGlobals
from toontown.toonbase import ToontownGlobals
from panda3d.otp import CFSpeech, CFTimeout
from toontown.battle import BattleProps
from toontown.battle import BattleParticles

# this allows the fucking chat noises to play
Suit.loadDialog(1)

def createSuit(cogType='f', customName=None):
	# Kobun42's very awesome create cog code
	# complete with a "custom name" function for you nerds
	# If you want to add level and class shit add setDisplayName to your code calling createSuit.
	# I do NOT recommend setting the custom name to have levels and class, do displayname instead.
	# cog.setDisplayName("Name\nBossbot\nLevel 69")
    cog = Suit.Suit() # create the entity
    cog.dna = SuitDNA.SuitDNA() # make the suit actually a suit lol
    cog.dna.newSuit(cogType) # cog type thingo
    cog.setDNA(cog.dna) # set the DNA to be the cog
    if customName:
        cog.setName(customName)
    else:
        if SuitBattleGlobals.SuitAttributes[cogType]:
            cog.setName(SuitBattleGlobals.SuitAttributes[cogType]['name'])
        else:
            print("For some fucking reason we couldn't find the cog name. Whatever, we'll name it 'Suit' for now.")
            cog.setName('Suit')
    cog.nametag3d.show()
    cog.addActive()
    cog.setPickable(0)
    cog.loop('neutral')
    return cog # coggers

cog = createSuit('ym')
cog.reparentTo(render)
cog.place()
cum = Sequence()
cum.append(Wait(10))
cum.append(Func(cog.setChatAbsolute, "I deliver.", CFSpeech | CFTimeout))
cum.play()

base.oobe()
base.run()

# by the way if you close this toonbase nags you about fucking toontown client respository just ignore it until i fucking fix it because disney's sticky taped code is headache inducing for me
# who knows if i even will
# will this be Kobun42's yandere simulator or even his Sellbot Field Offices? Probably tbh as it will never be completed.
