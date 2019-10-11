//===================================================================
// *** AGS MODULE HEADER ***
//
// Module: CatVentures
//
// Author: Juan M. Casillas <juanm.casillas@gmail.com>
//
// Copyright (C) 2019 Juan M. Casillas
//-------------------------------------------------------------------

//===================================================================
// Dependancies:
// The following constant definitions allow the compiler to check for
// module  dependencies and to issue appropiate error messages when a
// required module is not installed. There should be a definition for
// the current version and all previous compatiable versions. 
//-------------------------------------------------------------------

#define __CATVENTURES_MODULE__ 

// Define this module's version info
#define CatVentures_VERSION 0100
#define CatVentures_VERSION_0100

// Check for correct AGS version
#ifdef AGS_SUPPORTS_IFVER
#ifnver 2.72
#error Module CatVentures requires AGS V2.72 or above
#endif
#endif

// Check for required module/version 
// #ifndef RequiredModuleName_VERSION_0200
// #error Module ModuleName requires RequiredModuleName V2.00 or above
// #endif

//===================================================================
// Configuration:
// The following constant definitions are used to modify the behavior
// of this module.  
//-------------------------------------------------------------------
//Also change the Global Settings to Avoid Ctrl-X and so on.
//#define CAT_DEBUG 1
//#define CAT_NOINTRO 1

// game options.
// Avoid looking things from far away (player goes to the hotspot)
#define CATGAME_GOTOLOOKAT 1

#define CAT_PLAYER1_NAME		"Firulais"
#define CAT_PLAYER2_NAME		"Calcetines"
#define CAT_PLAYER3_NAME		"Miki"
#define CAT_PLAYER4_NAME		"Trufa"

#define CAT_PLAYER1_ID		0
#define CAT_PLAYER2_ID		1
#define CAT_PLAYER3_ID      2
#define CAT_PLAYER4_ID      3

#define CAT_DISABLED_ICON		121
#define CAT_FIRULAIS_ICON		213
#define CAT_CALCETINES_ICON	    214
#define CAT_MIKI_ICON			215
#define CAT_TRUFA_ICON			216		

#define CAT_NUM_PLAYERS         4

#define CAT_RAT_IDLE_VIEW 19

// TODO VIEWS

//===================================================================
// Return Values:
// The following constant definitions represent possible return value
// of functions contained in this module. 
//-------------------------------------------------------------------
//	#define ModuleName_RETURNVAL		100

//===================================================================
// Enumerated Types:
// The following enumerated data types are defined by this module. 
//-------------------------------------------------------------------
//	enum CatVentures_Type {
//		eCatVentures_Value1,
//		eCatVentures_Value2
//	};

struct PlayerInfo {
	int normal_view[5];
	int idle_view[5];
	int enabled_icon;
	int disabled_icon;
  bool added;
	Button *button;
	Character *character;
};

import PlayerInfo CatPlayers[CAT_NUM_PLAYERS];


//===================================================================
//
//-------------------------------------------------------------------

struct CatVentures {

	// Public Data
	//int VariableName;
  bool playersGUIEnabled;
  int playersRunning;
  
  // Quests
  bool QuestForRat; // Calcetines ask Firulais the Rat
  
  // Screeenshot
  String screenshot_template;
  int screenshot_counter;
  
  int GAME_STATE;
	// Public Static Methods
	//import static function FunctionNameStatic ();

	// Public Methods
	//import function FunctionNamePublic (); 

	import static void Init();
	import int PlayerToID(String Player);
	import void ChangePlayer (Character * c);
  import void AddPlayer(int playerID);

  import void EnablePlayersGUI();
  import void DisablePlayersGUI();
  
  import void SetNormalView(Character *c, int view=0);
  import void SetIdleView(Character *c, int view=0);
  
  import int GoToLookAt(String message);
  import int TakeScreenShot();
	// Private Data
	//protected int variable_name_protected;

	// Private Methods
	//protected import function function_name_protected ();
};

import CatVentures CatGame;