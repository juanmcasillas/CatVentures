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

    # explore the map, and build the rooms,
    # adding the different elements to be
    # rendered

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

    #
    # generate the PSD and PNG files, if the room exists (e.g. cutscenes are not generated)
    #

    for i in range(len(gmap.rooms)):
        room = gmap.rooms[i]
        if "room_m" in room.__dict__.keys() and room.room_m != None:
            rm.CreateRoom(room.iid, room.room_m)
