import requests

TEXT = 'text_transformation'
LINK = 'link_analysis'
INDEX = 'indexing'
DEFAULT_HEADERS = { 'user-agent': 'LimeH-Crawler' }

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
        # 2XX success, send to text transformation
        if target == TEXT:
            payload = {}
            url = ''
        # 4XX error, notify link analysis
        elif target == LINK:
            payload = {}
            url = ''
        # 4XX error, notify indexing
        elif target == INDEX:
            payload = {}
            url = ''
        else:
            return None
       return  requests.post(url, payload)

