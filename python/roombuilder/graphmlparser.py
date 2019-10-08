
import untangle
from . settings import Config

class Parser:
    def __init__(self):
        self.key_containers = [ "chars", "doors", "windows", "objects"]

    def ParseFile(self, fname):
        obj = untangle.parse(fname)
        obj = obj.graphml.graph
        
        # create my room object
        GameMap = type('', (object,), {})()
        GameMap.rooms = []
        # iterate over room nodes
        #  <node id="room_intro">
        #     <data key="name">Intro</data>
        #     <data key="desc">The intro cutscene</data>
        #     <data key="id">4</data>
        #     <data key="type">intro</data>
        # </node>
        for node in obj.node:
            room = type('', (object,), {})()
            room.iid = node['id']
            for k in self.key_containers:
                room.__dict__[k] = []
            for d in node.data:
                if d['key'] in self.key_containers:
                    # each key container has it's own XML format.
                    if d['key'] == "chars": room.chars = self.parseChars(d)
                    if d['key'] == "doors": room.doors = self.parseDoors(d)
                    if d['key'] == "windows": room.windows = self.parseWindows(d) 
                    if d['key'] == "objects": room.objects = self.parseObjects(d)

                else:
                    room.__dict__[d['key']] = d.cdata
            GameMap.rooms.append(room)

        return GameMap

    def parseChars(self, root):
        """
        <data key="chars">
           <char id="Firulais" state="normal"></char>
        </data>
        """
        ret = []
        for c in root.char:
            char = type('', (object,), {})()
            char.id = c['id']
            char.state = c['state']
            ret.append(char)
        return ret
        

    def parseDoors(self, root):
        """
        <data key="doors">
            <door id="1" position="left" type="FullOpen"/>
            <door id="2" position="right" type="Closed"/>
            <door id="3" position="front" type="Open" x="50" y="10" />
        </data>
        """
        ret = []
        for d in root.door:
            door = type('', (object,), {})()
            door.id = d['id']
            door.type = d['type']
            door.position = d['position']
            door.xpos = 0
            door.ypos = 0
            if door.position == "front":
                door.xpos = d['x']
                door.ypos = d['y']
            ret.append(door)
        return ret
        
    def parseWindows(self, root):
        """
        <data key="windows">
            <window id="1" position="front" x="50" y="10" bg="false"/>
            <window id="1" position="left" bg="true" hotspot="true"/>
        </data>
        """
        booleans = [ "bg", "hotspot" ]

        ret = []
        for w in root.window:
            window = type('', (object,), {})()
            window.id = w['id']

            for k in booleans:
                window.__dict__[k] = False
               
                if k in w._attributes.keys() and w[k].lower() == "true": 
                    window.__dict__[k] = True

            window.position = w['position']
            window.xpos = 0
            window.ypos = 0
            if window.position == "front":
                window.xpos = w['x']
                window.ypos = w['y']

            ret.append(window)
        return ret

    def parseObjects(self, root):
        """
        <data key="objects">
          <plantbig x="100" y="100" hotspot="true" behind="true"/>
          <radiator x="200" y="100"/>
        </data>
        """
        booleans = [ "behind", "hotspot" ]

        ret = []
        for o in root.object:
            obj = type('', (object,), {})()
            obj.id = o['id']
            obj.type = o['type']
            obj.xpos = o['x']
            obj.ypos = o['y']

            for k in booleans:
                obj.__dict__[k] = False
                if k in o._attributes.keys() and o[k].lower() == "true": 
                    obj.__dict__[k] = True

            ret.append(obj)
        return ret
        
    def Print(obj):
        for r in obj.rooms:
            print("room (iid):", r.iid)
            print(" -> name:",r.name)
            print(" -> desc:",r.desc)
            print(" -> id:",r.id)
            print(" -> type:",r.type)
            print(" -> chars")
            for c in r.chars:
                print("  * name:", c.id, "state:", c.state)
            print(" -> doors")
            for d in r.doors:
                print("  * id:", d.id, "type:", d.type, "position:", d.position, "xpos:", d.xpos, "ypos:", d.ypos)
            print(" -> windows")
            for w in r.windows:
                print("  * id:", w.id, "hotspot:", w.hotspot, "bg:", w.bg, "position:", w.position, "xpos:", w.xpos, "ypos:", w.ypos)                
            print(" -> objects")
            for o in r.objects:
                print("  * id:", o.id, "type:", o.type, "hotspot:", o.hotspot, "behind:", o.behind, "xpos:", o.xpos, "ypos:", o.ypos)                
            print("")            