import requests

def post_volume_up(url_base, control_url = 'Ds/Volume/control' ):
	r = requests.post('{0}/{1}'.format( url_base, control_url ) ,
		headers = {
			'soapaction': '"urn:av-openhome-org:service:Volume:1#VolumeInc"',
			'Cache-Control': 'no-cache',
			'Content-Type': 'text/xml; charset="utf-8"'
		},
		data = '<?xml version="1.0" encoding="utf-8"?>'
			'<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/"'
			's:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">'
				'<s:Body>'
				'<u:VolumeInc xmlns:u="urn:av-openhome-org:service:Volume:1"></u:VolumeInc>'
			'</s:Body>'
			'</s:Envelope>'
			)
	print r.status_code
	print r.text
