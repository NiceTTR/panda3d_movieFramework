# Stupid little Panda3d Animation Framework
This is some dumb little thing to ease me into using Panda3D for animations and the like.
To keep things simple I decided to use this with the TTO source rather than making things unusually complicated.

## How the heck do I use this?
Put this in the root directory of your Toontown source of choice. Don't forget for your source to have the appropriate resources as well otherwise it obviously wouldn't be able to run anything.
It's only been tested on Open Toontown as of now, but it SHOULD work for TTR, TTI, TTS, TTH, TTSH, or really any
traditional Toontown source with some minor alterations where necessary. If it doesn't work even with any necessary alterations made to fit with another source port, submit an issue with as much detail as possible and I might be able to help you out.

When you've done that, run it in Geany using the appropriate version of Panda3D for said source.
It should work if done correctly.

## Why should I use this compared to other Panda3D animation tools or my own code in general?
In my opinion, you really shouldn't be using this. This is just a little thing I made for testing purposes and I don't really think it's something people should use. There are way better ways to make a Panda3D animation.

## Confirmed Working Setups
- Open Toontown + Panda3D-1.11.0 (OpenToontown included version with panda3d.otp and panda3d.toontown modules)

## Theoretically Working Setups
- Any TTR-Based Code + Appropriate Panda3D Release (provided you replace the panda3d.otp and panda3d.toontown calls to where they'd fit on TTR)