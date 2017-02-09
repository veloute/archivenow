import requests
import logging
import os

PATH = str(os.path.dirname(os.path.abspath(__file__)))

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename=PATH + '/debug.log',
                    filemode='a')


# send http get request
def sendGetRequest(url, stream=False, headers=''):
	try:
                                    	  #URI's acually redirected by default
		r = requests.get(url, timeout=90, allow_redirects=True, stream=stream, headers=headers)
		return r
	except Exception as e:
		logging.error(e)
		return None

# send http post request
def sendPostRequest(uri, d, headers=''):
	try:
		r = requests.post(uri, timeout=90, data=d, allow_redirects=True,
						 headers=headers)
		return r
	except Exception as e:
		logging.error(e)
		return None
