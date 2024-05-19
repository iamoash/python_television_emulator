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
