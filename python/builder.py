#!/usr/bin/env python3

import argparse
import os

from roombuilder import *


if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument("-v", "--verbose", help="Show data about file and processing", action="count")
    #parser.add_argument("config_file", help="configuration file")
    args = parser.parse_args()

    settings.LoadConfig()
    settings.LOG.info("Builder config loaded.")
    if args.verbose:
        settings.Config.verbose = True

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