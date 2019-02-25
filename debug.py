
# Simple module for outputing formated errors and information


class Debug :
    def __init__ (self, level = 0) :
        self.ERROR = 0
        self.WARN = 2
        self.INFO = 3
        self.DEBUG = 4
        self.debugLevel = level

    def debug(self, level, message, log=False) :
        #print "D:", self.debugLevel, "M:", level
        if self.debugLevel >= level :
            msg = ''
            for i in range (0, level) :
                msg += "  "

            msg += "DEBUG LVL " + str(level) + " > " + message
            print msg
