import urllib2
from threading import Thread


# Crawler class
# Extends: threading.Thread
class Crawler(Thread):

	def __init__(self):
		pass

        # @override Thread.run()
        def run(self):
            pass

	# Input: String URL to grab
	# Behavior: 
	# Output: urllib2 request object
	def get_page(self, url):
		return urllib2.urlopen(url)


	# Input: urllib2.request object
	# Behavior:
        # Output: 
	def send_result(self, request):
		header = request.info()
		content = request.read()
		return


        # Input: None
        # Behavior: Request URL from queue
        # Output: 
	def request_url(self):
		pass



        # Input: Sleep duration in milliseconds
        # Behavior:
        # Output:
        def sleep(self, duration):
            pass

