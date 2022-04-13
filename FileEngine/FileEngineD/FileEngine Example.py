#welcome this is a file Engine Example
from FileEngineD import File_Engine

#first you Initilize it this is not needed in the R release or No_MB version

File_Engine.init()

#this will create the directory as described in the github this is mostly a development branch of file engine

#then take away the init after it is initnalized.

#now As Example
Health=3
File_Engine.save_file("PlayerHealth","Health",Health)
#now it will make a save wich can be called again at any time for games or updates
#it will also create a save History which dosnt happen in R And so on
#also as an example i did not remove the init as you see if your run it it will log!