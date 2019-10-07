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

    rm = RoomMaker()
    #rm.CreateRoom("first_01", NormalRoom("first"))
   
    room = NormalRoom("second")
    room.AddObject(Door("Front", "FullOpen"))
    room.AddObject(Door("Left", "Open"))
    room.AddObject(Door("Right", "Closed"))
    room.AddObject(Door("Bottom", "Closed"))

    room.AddObject(PlantBig((20, 100), behind=True, hotspot=False))
    room.AddObject(Radiator((60, 85), behind=False, hotspot=True))

    # dummy objects
    room.AddObject(RadiatorBig((183, 85), behind=False, hotspot=False))
    room.AddObject(Plant((250, 90), behind=False, hotspot=False))

    #rm.CreateRoom("second_02", room)

    # window one

    room_w = NormalRoom("third")
    room_w.AddObject(WindowSmall( (55,10), hotspot=False))
    room_w.AddObject(WindowSmall( (165,10), hotspot=True, bg=True))
    #rm.CreateRoom("third_03", room_w)

    # window two

    room_w = NormalRoom("fourth")
    room_w.AddObject(Window( "left", hotspot=False))
    room_w.AddObject(Window( "right", hotspot=True, bg=True))
    room_w.AddObject(Window( "front", hotspot=True, bg=True, coords=(55,10)))
    rm.CreateRoom("fourth_04", room_w)    