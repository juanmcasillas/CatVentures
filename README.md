# The Adventures Of Firulais & Calcetines (With Trufa and Miki)

A simple, short proof of concept to test [AGS (Adventure Game Studio)](https://www.adventuregamestudio.co.uk). The
plot is very simple: some cats live in a house, and they have to do things, just like the old "point and click" games. I get the look and feel of Lucasarts' Games (e.g. [Monkey Island](https://es.wikipedia.org/wiki/The_Secret_of_Monkey_Island), [Maniac Mansion](https://en.wikipedia.org/wiki/Maniac_Mansion)) with some improvements of [Thimbleweed Park](https://en.wikipedia.org/wiki/Thimbleweed_Park) the last game written by **Ron Gilbert** and **David Fox**.

<a href="https://youtu.be/IPjfnaJqFXc">Demo video on YouTube</a>

This project uses [AGS (Adventure Game Studio)](https://www.adventuregamestudio.co.uk) as development framework. AGS has two parts, the **engine** that runs on Windows, MacOS, Linux, PSP (among others) and the **editor** that sadly, only runs on Windows, but they are trying to refactor all the code and do it more portable. I use the latest version available, **3.5.0**.

In order to implement the LucasArt's interface, I modify the [TumbleWeed Vers](https://github.com/dkrey/ags_tumbleweed) template from **drkey**. These template provides the basics of a 9-verb interface, just like the latest Thimbleweed Park or The Day of The Tentacle.

**NOTES**:

* The game is designed in the old-but-good **320x200** mode. 
* Graphics are somewhat crap, but I'm not graphic designer. 
* English translation ... well, you know; english level: medium.
* Sounds are picked from internet.
* Assets included.

# Table Of Contents

1. [Project Features](#project-features)
2. [Download](#download)
3. [Instructions](#instructions)
4. [Python room generator](#python-room-generator)

# Project features

The "main" features of this game are:

1. Support for 9-verb interface, fully localized, with button adaptation to the locale. See [issues](https://github.com/dkrey/ags_tumbleweed/issues?q=is%3Aopen+is%3Aissue) for more detailed info about that.
2. Support up to for players (cats) at the same time, just like Thimbleweed park, Maniac Mansion or The Day Of the Tentacle. I modify the template and write some custom code to provide a new interface with keyboard shorcuts.
3. Python-Based semi-procedural room generation. **See below** (that's interesting).
4. Test all the major aspects of this kind of game development:
    1. Multiple rooms and navigation.
    2. Open/Close/Locked doors.
    3. Multiple-Level dialogs (with code inside).
    4. Overhead map.
    5. Multiple player coordination.
    6. Inventory Management.
    7. "Sound". (I pick some random noises from the internet to test it).
    8. Cutscenes (intro, ending).
    9. Custom text render.
   10. The pain-in-the-ass of drawing graphics.
   11. Animations.
   12. Localization (currently only english and spanish)


2. [Download](#download)

The AGS engine runs on **Android, iOS, Linux, Mac OS X, PSP and Windows**. See their [github page](https://github.com/JanetGilbert/ags) for instructions and building. The engine is used to run the game. So if you plan to run this game on that platforms, take a read. 

On **Windows** and **Linux** is pretty straighforward: go to the [Releases Page](https://github.com/juanmcasillas/CatVentures/releases), download the latest binary, and try it, quick, and dirty. In other platforms, you need the engine compiled.

# text encoding: windows1250 (to get the special spanish chars)

* use thimbleweed theme


 # button verb font
http://www.cheapprofonts.com/Familiar_Pro
13 pt, crisp

Replaced the verbs PickUp and Push so the string "empujar" fits in the middle. `verbgui.asc:1201`

```
ES
50x12
    Abrir
    Cerrar
    Dar
    Empujar
    Tirar
    Usar
56x12
    Coger
    Mirar
    Hablar

50x12
    Open
    Close
    Give
    Push
    Pull
    Use
56x12
    Pick Up
    Look At
    Talk To
EN
```

# python roomgen

created a simple framework that builds the rooms for you, from an XML file (GraphML) that can be visualized
by any tool (e.g yEd). The XML parser uses `untangle` a decent and fast XML->Obj tool.

