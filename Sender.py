import requests
import re
import jsonizer
import datetime
import requests

TEXT = 'text_transformation'
LINK = 'link_analysis'
INDEX = 'indexing'
DEFAULT_HEADERS = { 'user-agent': 'LimeH-Crawler' }
ACCESS_TIME = r'[Dd]ate:\s?'
FORWARD_ADDRESS = ''

# Send message to text transformation, link analysis or indexing depending on response crawler received
class Sender:

    @staticmethod
    def TEXT():
        return TEXT

    @staticmethod
    def LINK():
        return LINK
    
    @staticmethod
    def INDEX():
        return INDEX

    @staticmethod
    def send_request(target, request, url):
        payload = {}
        access_time = ''
        # 2XX success, send to text transformation
        if target == TEXT:
            access_time = datetime.datetime.utcnow().replace(microsecond=0).isoformat() + 'Z'
            content = request.read()
            forward_address = '' #request.headers['access-time']
            payload = {
                    'url': url,
                    'metadata': {
                        'access_time': access_time,
                        'forward address': forward_address
                        },
                    'content': { content }
                    }
        # 4XX error, notify link analysis
        elif target == LINK:
            payload = {}
            url1 = 'http://green-eth.cs.rpi.edu/crawling'
            url2 = ''
        # 4XX error, notify indexing
        elif target == INDEX:
            payload = {}
            url = ''
        else:
            return None
        #return requests.post(url, payload)

