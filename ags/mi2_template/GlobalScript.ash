// Main header script - this will be included into every script in
// the game (local and global). Do not place functions here; rather,
// place import definitions and #define names here to be used by all
// scripts.

//		Modes definition.              
//-----------------------------------------------------
#define DEFAULT -1// DO NOT CHANGE OR REMOVE THIS LINE

//define below all the modes you are going to use, giving
//to each one its own unique name and id.
//Names you define here will be the ones you will use to
//set or check modes.

//	Mode	Id
#define WALK	0
#define LOOK 	1
#define TALK 	2
#define PICKUP 	3
#define OPEN 	4
#define CLOSE 	5
#define PUSH 	6
#define PULL 	7
#define USE 	8
#define GIVE 	9
#define SAIL 	10// you can delete this one, it was just for the template demo.
//-----------------------------------------------------

//		Template functions:
//-----------------------------------------------------
//Setting and checking modes:
import function SetDefaultMode(int mode);
import function SetMode(int mode);
import function UsedMode(int mode);
import function UsedInvMode(int mode, int item);
//Checking current translation:
import function Translation(const string language);
//Map rooms:
import function StartMapRoom();
import function EndMapRoom();
//Cancelable semi-blocking move-player-character functions:
import function MovePlayerEx(int x, int y, int direct);
import function MovePlayer(int x, int y);
import function Go();
//Move player to something (rather than coords) functions:
import function GoToCharacterEx(int charidwhogoes, int charidtogo, int direction, int xoffset, int yoffset, int NPCfacesplayer, int blocking);
//import function GoToCharacterEx(int charid, int direction, int xoffset, int yoffset, int NPCfacesplayer, int blocking);
import function GoToCharacter(int charid, int direction, int NPCfacesplayer, int blocking);
import function GoTo(int blocking);
//running unhandled events in shared interactions:
import function Unhandled();
//-----------------------------------------------------// Automatically converted interaction variables
import int IntVar_Global_1;
