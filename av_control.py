import requests

def join_dicts(x, y):
    '''Given two dicts, merge them into a new dict as a shallow copy.'''
    z = x.copy()
    z.update(y)
    return z

def default_headers():
	return dict({
			'Cache-Control': 'no-cache',
			'Content-Type': 'text/xml; charset="utf-8"'
		})

def post_volume_up(url_base, control_url = 'Ds/Volume/control' ):
	r = requests.post('{0}/{1}'.format( url_base, control_url ) ,
		headers = join_dicts( default_headers(), {
			'soapaction': '"urn:av-openhome-org:service:Volume:1#VolumeInc"'
		} ),
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

def post_volume_down(url_base, control_url = 'Ds/Volume/control' ):
	r = requests.post('{0}/{1}'.format( url_base, control_url ) ,
		headers = join_dicts( default_headers(), {
			'soapaction': '"urn:av-openhome-org:service:Volume:1#VolumeDec"',
		} ),
		data = '<?xml version="1.0" encoding="utf-8"?>'
			'<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/"'
			's:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">'
				'<s:Body>'
				'<u:VolumeDec xmlns:u="urn:av-openhome-org:service:Volume:1"></u:VolumeDec>'
			'</s:Body>'
			'</s:Envelope>'
			)
	print r.status_code
	print r.text

def radio_play(url_base, control_url = 'Ds/Radio/control'):
	r = requests.post('{0}/{1}'.format( url_base, control_url ) ,
		headers = join_dicts( default_headers(), {
			'soapaction': '"urn:av-openhome-org:service:Radio:1#Play"',
		} ),
		data = '<?xml version="1.0" encoding="utf-8"?>'
			'<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/"'
			's:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">'
				'<s:Body>'
				'<u:Play xmlns:u="urn:av-openhome-org:service:Radio:1"></u:Play>'
			'</s:Body>'
			'</s:Envelope>'
			)
	print r.status_code
	print r.text


def radio_stop(url_base, control_url = 'Ds/Radio/control'):
	r = requests.post('{0}/{1}'.format( url_base, control_url ) ,
		headers = join_dicts( default_headers(), {
			'soapaction': '"urn:av-openhome-org:service:Radio:1#Stop"',
		} ),
		data = '<?xml version="1.0" encoding="utf-8"?>'
			'<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/"'
			's:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">'
				'<s:Body>'
				'<u:Stop xmlns:u="urn:av-openhome-org:service:Radio:1"></u:Stop>'
			'</s:Body>'
			'</s:Envelope>'
			)
	print r.status_code
	print r.text

