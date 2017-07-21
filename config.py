


class Loaders:

	# A dict of the loader skins, and the skins they need to load. Along with the coordinates the skins need to be set to. 
	# If a skin sets it's own coordinates, you can set the skins coordinate to False and it won't be moved.
	# The skins in your theme do not need to all be from the same parent skin. You can mix illustro, homebrew, etc. Just make sure you put the correct config names in.
	# "Loader Name" : {
	#	"ConfigToBeLoaded" : [x,y],
	#   "ConfigToBeLoaded" : False
	# }
	# You can run GenLoaders.py to generate all of the loader skins.
	# They will be generated in the Loaders folder, and the skins will be called LoaderNameLoader \ LoaderNameUnloader \ LoaderNameRefresher
	# The initial setup of these can be a bit tedious, but once it's setup, modifying it is very simple.
	skins = {
		"LoginScreen" : {
			"LoginScreen\LoginScreenBackground"  :[0,     0],
			"LoginScreen\LoginScreenUserSelector" :False
		},
		
		"LoginScreenTest" : {
			"LoginScreen\YamaWallpaper" : [0,     0],
			"Illustro\Clock"            : [142, 129],
			"Illustro\Disk"             : [420, 590],
			"Illustro\Google"           : [819, 249],
			"Illustro\Recycle Bin"      : [991, 660]
		},
		
		"LoginScreenTest2" : {
			"LoginScreen\YamaWallpaper" : [0,     0],
			"Illustro\Clock"            : [552, 342],
			"Illustro\Disk"             : [981, 234],
			"Illustro\Google"           : [120, 592],
			"Illustro\Recycle Bin"      : [321, 523]
		},
		
		"LoginScreenTest3" : {
			"LoginScreen\YamaWallpaper" : [0,     0],
			"Illustro\Clock"            : [912, 412],
			"Illustro\Disk"             : [931, 342],
			"Illustro\Google"           : [423, 931],
			"Illustro\Recycle Bin"      : [943, 432]
		}
	}


class Users:
	
	# A dict of all the users you want to generate.
	# USER: {
	#	"loader"   : "your custom loader config",
	#	"password" : "User's Password",
	#	"image"    : "Path to user profile picture. Relative to the loginscreen skin"
	# }
	# You can use GenUserPictures.py to generate all of the user skins in the LoginScreenUserPicture folder, with the file names being the user name.
	# GenUserSelector.py will re-create a LoginScreenUserSelector skin using this information, so make sure all of the profiles you want access to are in this dict.
	users = {
		"tester": {
			"loader"   : "LoginScreen\LoginScreenTestLoader",
			"password" : "password",
			"image"    : "#@#Images\SpicyDefault.png"
		},
		"tester2": {
			"loader"   : "LoginScreen\LoginScreenTest2Loader",
			"password" : "password",
			"image"    : "#@#Images\SpicyDefault.png"
		},
		"tester3": {
			"loader"   : "LoginScreen\LoginScreenTest3Loader",
			"password" : "password",
			"image"    : "#@#Images\SpicyDefault.png"
		}
		
	}