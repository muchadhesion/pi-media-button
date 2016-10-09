#!/usr/bin/env python

import av_control
import time

def test_volume_up():
	av_control.post_volume_up('http://192.168.1.84:55178')

def test_radio_play():
	av_control.radio_play('http://192.168.1.84:55178')
	time.sleep(2)
	av_control.radio_stop('http://192.168.1.84:55178')

def test_find_button_device(name):
	device = find_button_device(name)
	if device == None:
		raise Exception("Test Failed to find "+name)

def devices():
	import evdev
	devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
	return devices

def find_button_device(name):
	for device in devices():
		print(device.phys, device.name, device.fn, device.info)
		if device.name == name:
			return device
	return None


if __name__ == "__main__":
	import sys
	import evdev

	button_name = 'Satechi Media Button'
	button = find_button_device(button_name)
	if button == None:
		if len(devices()) == 0:
			print "No devices found, try running with sudo"
		print "Can't find {}".format(button_name)
		sys.exit(1)

	button.grab()
	for event in button.read_loop():
		if event.type == evdev.ecodes.EV_KEY and event.value == evdev.KeyEvent.key_down:
			print(evdev.categorize(event))
			if event.code == evdev.ecodes.KEY_VOLUMEUP:
				av_control.post_volume_up('http://192.168.1.84:55178')
			elif event.code == evdev.ecodes.KEY_VOLUMEDOWN:
				av_control.post_volume_down('http://192.168.1.84:55178')
			elif event.code == evdev.ecodes.KEY_PLAYPAUSE:
				av_control.radio_play('http://192.168.1.84:55178')
