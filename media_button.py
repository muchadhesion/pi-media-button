#!/usr/bin/env python

import av_control
import time

def test_volume_up():
	av_control.post_volume_up('http://192.168.1.84:55178')

def test_radio_play():
	av_control.radio_play('http://192.168.1.84:55178')
	time.sleep(2)
	av_control.radio_stop('http://192.168.1.84:55178')

if __name__ == "__main__":
	import sys
	import evdev

	devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]

	if len(devices) == 0:
		print "No devices found, try running with sudo"
		sys.exit(1)


		for device in devices:
			print(device.phys, device.name, device.fn, device.info)
			if device.name == 'Satechi Media Button':
				print(device)
				device.grab()
				for event in device.read_loop():
					if event.type == evdev.ecodes.EV_KEY:
						print(evdev.categorize(event))
