import requests


TEXT = 'text_transformation'
LINK = 'link_analysis'
INDEX = 'indexing'
DEFAULT_HEADERS = { 'user-agent': 'LimeH-Crawler' }
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
    def send_request(target, headers, payload):
        print("headers: " + str(headers))
        if target == TEXT:
            print("Got 2XX sending to " + TEXT)
            

        elif target == LINK:
            pass
        elif target == INDEX:
            pass
        else:
            return None

