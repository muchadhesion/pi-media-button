#!/usr/bin/env python


import requests

def post_volume_up(url_base, control_url = 'MediaRenderer/RenderingControl/control' ):
	r = requests.post('{0}/{1}'.format( url_base, control_url ) ,
		headers = {
			'soapaction': 'SoapAction:urn:schemas-upnp-org:service:RenderingControl:1#GetVolume',
			'Cache-Control': 'no-cache',
			'Content-Type': 'text/xml; charset="utf-8"'
		},
		data = '<?xml version="1.0" encoding="utf-8"?>'
			'<s:Envelope s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/" xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">'
			'<s:Body>'
			'<ns0:GetVolume xmlns:ns0="urn:schemas-upnp-org:service:RenderingControl:1">'
			'<InstanceID>0</InstanceID>'
			'<Channel>Master</Channel>'
			'</ns0:GetVolume>'
			'</s:Body>'
			'</s:Envelope>'
		)

	print r.status_code
	print r.text




def test_volume_up():
	post_volume_up('http://192.168.1.84:55178')


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



