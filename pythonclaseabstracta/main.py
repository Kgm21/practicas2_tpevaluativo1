from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self,isOpen,isPlaying,volume): 
        print("The Player constructor was invoked.")
        self.isOpen = isOpen
        self.isPlaying = isPlaying
        self.volume = volume
        self.setVolume = 10

    def _del_(self):
        print("The Player destructor was invoked.")
    
    def open(filePath): 
        pass

    def play(self):
        self.isPlaying = True
        print("The audiofile is playing.")

    def stop(self):
        self.isPlaying =False
        print("The audiofile is stopped.")
    
    def setVolume(self, value):
        self.volume = value
        print(f"The volume value is: {value}")

class VLC(Player):
    def __init__(self, isOpen, isPlaying, volume):
        super().__init__(isOpen, isPlaying, volume)
        print("The VLC constructor was invoked.")
    
    def _del_(self):
        print("The VLC destructor was invoked.")

    def open(self,filePath): 
        self.isOpen = True
        print(f"The audiofile: {filePath} is open")

    def setPitch(self,value):
        self.pitch = value
        print(f"The pitch value is:  {self.pitch}")


class Winamp(Player):
   
    print("The Winamp constructor was invoked.")
    def open(self,filePath):
        self.isOpen = filePath
        print("the audiofile:  {filePath} is open")

    def play(self,filePath):
        self.isOpen = True
        print(f"The audiofile: {filePath}  is open")
    
    def setVolume(self, value):
        self.volume = value
        print(f"The volume value is: {value} ")


vlcPlayer =VLC(None,5,0)
vlcPlayer.open("./resources/orchestral.ogg")
vlcPlayer.play()
vlcPlayer.setVolume(13)
winampPlayer = Winamp(None,None,0)
winampPlayer.open("./resources/orchestral.ogg")
winampPlayer.play()
winampPlayer.setVolume(13)



        