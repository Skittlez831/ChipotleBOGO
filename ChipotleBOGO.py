import requests

ZIPCODE = ''
FIRSTNAME = ''
LASTNAME = ''
PHONENUMBER = ''

headers = {
    'origin': 'https://savorwavs.com',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.8',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    'content-type': 'application/json;charset=UTF-8',
    'accept': 'application/json',
    'referer': 'https://savorwavs.com/buy-one-get-one',
    'authority': 'savorwavs.com',
}

data = '{"zip":"' + ZIPCODE + '","firstName":"' + FIRSTNAME + '","lastName":"' + LASTNAME + '","phoneNumber":"+1' + PHONENUMBER + '","optedIn":false}'

r = requests.post('https://savorwavs.com/api/offer/request', headers=headers, data=data)
if r.status_code == 200:
	print 'Success, text message sent to {}'.format(PHONENUMBER)
else:
	print 'Failed, text message was not sent to {}'.format(PHONENUMBER)