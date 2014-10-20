
class Clock (object):
	#Init
    def __init__ (self,time):
    	self._time = time
        self._register = {}

    #Extract Attributes:
    def time(self):
    	return self._time
    def register(self):
    	return self._register

    #Functions
    def register(self, f, priority):
    	self._register[f] = priority
    def tick(self):
    	Order = sorted(self._register, key=self._register.get)
    	for f in Order:
    		self._register[f]

# Used For Testing:
# def test():
# 	Testclock = Clock(0)
# 	Testclock.register(Testclock.time(), 1)
# 	Testclock.register(Testclock.time(), 2)
# 	Testclock.register(Testclock.time(), 2)
# 	Testclock.register(Testclock.time(), 1)
# 	Testclock.tick()

# if __name__ == '__main__':
# 	test()