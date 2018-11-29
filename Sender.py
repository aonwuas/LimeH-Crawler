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
        if target == TEXT:
            print("Got 2XX sending to " + TEXT)
            print("HEADERS:\n" + str(headers))
        elif target == LINK:
            print("Got 4XX telling " + LINK)
        elif target == INDEX:
            print("Got 4XX telling " + INDEX)
        else:
            return None

