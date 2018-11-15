import urllib2, httplib
from threading import Thread
import time

# Link to url request endpoint

# Crawler class
# Extends: threading.Thread
class Crawler(Thread):

	def __init__(self, id, URL):
            super(Crawler, self).__init__()
            self.iden = str(id)
            self.URL = URL

        # @override Thread.run()
        def run(self):
            print("Crawler " + self.iden + " started")
            while(True):
                r = self.request_url()
                if r is None:
                    print("Crawler " + self.iden + ": URL endpoint not found. Sleeping for 5 seconds")
                    self.sleep(5000)


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
            #print('requesturl')
            try:
                #print("URL: " + self.URL)
                self.URL = 'lime-h.cs.rpi.edu'
                conn = httplib.HTTPConnection(self.URL, 8081, timeout=10)
                #print("Crawler " + self.iden + ": attemping to get url from " + self.URL)
                conn.request('POST', '/url', {}, {})
                #print('r')
                response = conn.getresponse()
                if response is None:
                    print("Failed to get a response")
                    return None
                if response.status == '200 OK':
                    url = response.read()
                    if url != "":
                        self.send_result(page_request(url))
                    else:
                        sleep(100)
                        return true
            except Exception as e:
                print(str(e))
                return None


        # Input: Sleep duration in milliseconds
        # Behavior:
        # Output:
        def sleep(self, duration):
            time.sleep(duration/1000)

