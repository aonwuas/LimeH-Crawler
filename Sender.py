import requests

# Still needs error handling

class Sender:
	request = None

        def __init__(self):
            return

	class Request:
		target = None
		payload = None


		def __init__(self, url):
		    self.target = url
		
		def add_payload(self, payload):
		    self.payload = payload	
                    pass

		def send_post(self):
                        r = requests.post(self.target, self.payload)
                        return r.status_code


	def make_request(self, url):
		if request is None:
			self.request = self.Request(url)
		else:
			# Complete or delete current request
			pass


        def set_payload(self, payload):
            pass

	def send:
		if request is not None:
                    return self.request.send_post()
		else:
			pass

        def reset_request:
                request = None
                return
