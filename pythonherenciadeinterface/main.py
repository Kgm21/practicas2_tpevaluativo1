from abc import abstractmethod
from abc import ABCMeta

class Player:
    def open(filePath):
        pass
    def play():
        pass
    def stop():
        pass
    def setVolume():
        pass

class PlayerPitchable:
    def setPitch(pitch):
        pass

class VLC(Player,PlayerPitchable):
    def __init__(self,isOpen,isPlaying,volume): 
        print("The VLC constructor was invoked.")
        self.isOpen= False
        self.isPlaying = False
        self.setVolume(10)
    
    def _del_(self):
        print("The VLC destructor was invoked.")
    
    def open(self,filePath):
        self.isOpen = True
        print(f"The audiofile:  {filePath} is open.") 
    
    def play(self):
        self.isPlaying = True
        print("The audiofile is playing.")
    
    def stop(self):
        self.isPlaying = False
        print("The audiofile is stopped.")
    
    def setVolume(self,value):
        volume = value
        print(f"The volume value is: {volume}")
    
    def setPitch(self,value):
        pitch = value
        print(f"The pitch value is:{pitch}")


vlcPlayer = VLC(None,None,0)
vlcPlayer.open("./resources/orchestral.ogg")
vlcPlayer.play()
vlcPlayer.setVolume(13)

    
    

