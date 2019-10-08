#!/usr/bin/env python3

import argparse
import os
import sys

from roombuilder import *


if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument("-v", "--verbose", help="Show data about file and processing", action="count")
    parser.add_argument("gamemap", help="GRAPHML map with the rooms")
    args = parser.parse_args()

    settings.LoadConfig()
    settings.LOG.info("Builder config loaded.")
    if args.verbose:
        settings.Config.verbose = True

    gmap = Parser().ParseFile(args.gamemap)
    Parser.Print(gmap)         

    rm = RoomMaker()
    rooms = []

    for i in range(len(gmap.rooms)):
        room = gmap.rooms[i]
        r = None
        if room.type == "intro": continue
        if room.type == "normal": r = NormalRoom(room.name)
        if room.type == "long": r = LongRoom(room.name)

        for d in room.doors:
            r.AddObject(Door(d.position, d.type, coords=(d.xpos,d.ypos)))        

        for w in room.windows:
            if w.type == "small": r.AddObject(WindowSmall( (w.xpos,w.ypos), hotspot=w.hotspot, bg=w.bg))      
            if w.type == "normal": r.AddObject(Window( w.position, hotspot=w.hotspot, bg=w.bg, coords=(w.xpos,w.ypos)))  

        # xy objects are created using the factory
        for o in room.objects:
            if o.type in settings.Config.objectFactory.keys():
                object_f = settings.Config.objectFactory[o.type]
                r.AddObject(object_f( (o.xpos,o.ypos), behind=o.behind, hotspot=o.hotspot))

        gmap.rooms[i].room_m = r


    for i in range(len(gmap.rooms)):
        room = gmap.rooms[i]
        if "room_m" in room.__dict__.keys() and room.room_m != None:
            rm.CreateRoom(room.iid, room.room_m)

    sys.exit(0)
    # working test.

    # empty room
    rm = RoomMaker()
    rm.CreateRoom("first_01", NormalRoom("first"))
   
    # door room
    room = NormalRoom("second")
    room.AddObject(Door("Front", "FullOpen", coords=(130,12)))
    room.AddObject(Door("Left", "Open"))
    room.AddObject(Door("Right", "Closed"))
    room.AddObject(Door("Bottom", "Closed", coords=(150,146)))

    room.AddObject(PlantBig((20, 100), behind=True, hotspot=False))
    room.AddObject(Radiator((60, 85), behind=False, hotspot=True))
    # dummy objects
    room.AddObject(RadiatorBig((183, 85), behind=False, hotspot=False))
    room.AddObject(Plant((250, 90), behind=False, hotspot=False))
    rm.CreateRoom("second_02", room)

    # window small
    room = NormalRoom("third")
    room.AddObject(WindowSmall( (55,10), hotspot=False))
    room.AddObject(WindowSmall( (165,10), hotspot=True, bg=True))
    rm.CreateRoom("third_03", room)

    # window big
    room = NormalRoom("fourth")
    room.AddObject(Window( "left", hotspot=False))
    room.AddObject(Window( "right", hotspot=True, bg=True))
    room.AddObject(Window( "front", hotspot=True, bg=True, coords=(55,10)))
    rm.CreateRoom("fourth_04", room)    

    # long room, doors
    room = LongRoom("room5")
    room.AddObject(Door("Front", "FullOpen", coords=(330,12)))
    room.AddObject(Door("Front", "Open", coords=(130,12)))
    room.AddObject(Door("Front", "Closed", coords=(230,12)))
    room.AddObject(Door("Left", "Open"))
    room.AddObject(Door("Right", "Closed"))
    room.AddObject(Door("Bottom", "Closed", coords=(250,146)))
    rm.CreateRoom("five_05", room)

    # long room, windows
    room = LongRoom("room6")
    room.AddObject(Window( "left", hotspot=False))
    room.AddObject(Window( "right", hotspot=True, bg=True))
    room.AddObject(Window( "front", hotspot=True, bg=True, coords=(55,10)))
    rm.CreateRoom("five_06", room)