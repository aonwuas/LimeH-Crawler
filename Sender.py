import requests
import re

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
    def send_request(target, headers, content):
        payload = {}
        url = ''
        access_time = ''
        # 2XX success, send to text transformation
        if target == TEXT:
            url = 'url'
            for line in str(headers).split('\n'):
                if re.match(ACCESS_TIME, line):
                    access_time = re.sub(ACCESS_TIME, "", line)
                    print(line)
            forward_address = 'forward_address'
            payload = {
                    'metadata': {
                        'url': url,
                        'access_time': access_time,
                        'forward address': forward_address
                        }
                    }
           # print(payload)
           # print(headers)
        # 4XX error, notify link analysis
        elif target == LINK:
            payload = {}
            url = 'http://green-eth.cs.rpi.edu/crawling'
        # 4XX error, notify indexing
        elif target == INDEX:
            payload = {}
            url = ''
        else:
            return None
        #return requests.post(url, payload)

