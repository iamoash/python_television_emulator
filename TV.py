class TV:
    def __init__(self):
        self.channel = 1         #Sets the Channel to 1
        self.volumelevel = 1     #Sets the Volume to 1
        self.on = False          #Sets to False if the TV Turns off

  # A process that returns True when TV is on
    def turnOn(self):
        self.on = True

    # A Process that returns False when TV is off
    def turnOff(self):
        self.on = False
    
    # A Process that returns the current channel
    def getChannel(self):
        return self.channel
    
    # A Process that sets new channel
    def setChannel(self, channel):
        if self.on and (1 <= channel <= 120): # sets channel iff TV is turned on
            self.channel = channel
  
    # A Process that returns the current volume
    def getVolume(self):
        return self.volumeLevel
    
    # A Process that sets new volume level
    def setVolume(self, volume):
        if self.on and (1 <= volume <= 7):
            self.volumeLevel = volume
            
    # A Process  that increments channel number by 1
    def channelUp(self):
        if self.on and self.channel < 120:          
            self.channel += 1

    # A Process the decrements channel number by 1
    def channelDown(self):
        if self.on and self.channel > 1:             
            self.channel -= 1

    # A Process that increments volume level by 1
    def volumeUp(self):
        if self.on and self.volumeLevel < 7:         
            self.volumeLevel += 1

    # A Process the decrements volume level by 1
    def volumeDown(self):
        if self.on and self.volumeLevel > 1:         
            self.volumeLevel -= 1