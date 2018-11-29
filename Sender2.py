import requests


TEXT_TRANSFORMATION = ""
LINK_ANALYSIS = ""
INDEXING = ""
class Sender:

    def targets(target_string):
        if target_string == "text_transformation":
            pass
        elif target_string == "link_analysis":
            pass
        elif target_string == "indexing":
            pass
        else:
            return None

    def send_request(target, headers, payload):
        target_info = targets(target)
        if target_info is not None:
            pass
        result = requests.post(target, data = payload)
        return result


    def default_headers():
        return { 'user-agent': 'LimeH-Crawler' }
