
class Clock (object):
	#Init
    def __init__ (self,time):
    	self._time = time
        self._register = {}

    #Extract Attributes:
    def time(self):
    	print self._time
    	return self._time
    def register(self):
    	return self._register

    #Functions
    def add_to_register(self, f, priority):
    	self._register[f] = priority
    def tick(self):
    	Order = sorted(self._register, key=self._register.get)
    	for f in Order:
    		f(self._time)
    	self._time += 1

# # Used For Testing:
# def test():
# 	Testclock = Clock(0)
# 	Testclock.tick()

# if __name__ == '__main__':
# 	test()