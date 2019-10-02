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
	#define CatVentures_CONFIGPARAM		10


//===================================================================
// Return Values:
// The following constant definitions represent possible return value
// of functions contained in this module. 
//-------------------------------------------------------------------
	#define ModuleName_RETURNVAL		100


//===================================================================
// Enumerated Types:
// The following enumerated data types are defined by this module. 
//-------------------------------------------------------------------
	enum CatVentures_Type {
		eCatVentures_Value1,
		eCatVentures_Value2
	};


//===================================================================
   struct CatVentures  {
//
// The following structure contains the definition of a menu item.
//-------------------------------------------------------------------
	// Public Data
	int	VariableName;

	// Public Static Methods
	import static function FunctionNameStatic();

	// Public Methods
	import function FunctionNamePublic();
  
  import static function Say1();

   	// Private Data
	protected int	variable_name_protected;

	// Private Methods
	protected import function function_name_protected();
};
