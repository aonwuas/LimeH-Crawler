import urllib2, httplib
from threading import Thread
import time

# Link to url request endpoint
URL = 'lime-h.cs.rpi.edu/url'

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
	def page_request(self, url):
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
	    conn = httplib.HTTPConnection(URL)
            conn.request('POST', "", None, None)
            response = conn.getresponse()
            if response.status == '200 OK':
                url = response.read()
                if url != "":
                    send_result(page_request(url))
                else:
                    sleep(100)


        # Input: Sleep duration in milliseconds
        # Behavior:
        # Output:
        def sleep(self, duration):
            time.sleep(duration/1000)

