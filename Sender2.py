import requests

class Sender:
    def send_request(target, headers, payload):
        result = requests.post(target, data = payload)
        return result


    def default_headers():
        return { 'user-agent': 'LimeH-Crawler' }
