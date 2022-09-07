#!/usr/bin/python3

# import modules
import os, time, random
from multiprocessing import Process
from pynput.mouse import Controller as MouseController

# helper functions
def randint(i, v):
	 return random.randint(i, v)

emulate_process = None

def emulate():
	mouse = MouseController()	# get mouse controller object
	mouse.position = (0, 0)		# set mouse cursor initial position
	
	# start the infinite loop 
	while True:
		# mouse cursor movement
		random_x_mouse_move = randint(1, 10)
		random_y_mouse_move = randint(1, 10)
		mouse.move(random_x_mouse_move, random_y_mouse_move)
		
		# mouse scroll wheel movement
		random_x_mouse_scroll = randint(-3, 3)
		random_y_mouse_scroll = randint(-3, 3)
		mouse.scroll(random_x_mouse_scroll, random_y_mouse_scroll)
		
		# pause in-between each movements (in seconds)
		random_movement_sleep_duration = randint(1, 10)
		time.sleep(random_movement_sleep_duration)

def colored(r, g, b, text):
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"

def ui_user_options():
	global emulate_process
	
	text = ""
	if emulate_process is None:
		text += colored(255, 255, 255, "PROGRAM STATUS: ") + colored(255, 0, 0, "OFF")
	else:
		text += colored(255, 255, 255, "PROGRAM STATUS: ") + colored(0, 255, 0, "ON")
	
	text += colored(255, 255, 255, "\nPRESS ENTER TO TOGGLE")
	text += "\n"
	
	return input(text)
	
def toggle_emulation_state():
	global emulate_process
	
	if emulate_process is None:
		emulate_process = Process(target = emulate, args = (), daemon = True);	
		emulate_process.start()
	else:
		emulate_process.terminate()
		emulate_process = None

while True:
	os.system('clear')
	ui_user_options();
	toggle_emulation_state();
