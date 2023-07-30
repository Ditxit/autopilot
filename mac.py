#!/usr/bin/python3

# import modules
import time, random
import macmouse

# helper functions
def randint(i, v):
    return random.randint(i, v)

while True:
	# mouse cursor movement
	macmouse.move(
		x = randint(-25, 25),
        y = randint(-25, 25),
	    absolute = False,
	    duration = randint(1, 2),
	    steps_per_second = randint(30, 120)
	)
						
	# mouse scroll wheel movement
	macmouse.wheel(randint(-4, 4))
			
	# pause in-between each movements (in seconds) 
	time.sleep(randint(1, 4))
