import requests

# Still needs error handling

class Sender:
	request = None

	class Request:
		target = None
		payload = None


		def __init__(self, url):
			self.target = url
		
		def add_payload(self, payload):
			pass

		def send_post(self):
			pass

	def make_request(self, url):
		if request is None:
			request = self.Request(url)
		else:
			# Complete or delete current request
			pass


        def set_payload(self, payload):
            pass

	def send_request:
		if request is not None:
			pass
		else:
			pass

        def reset_request:
                request = None
                return
