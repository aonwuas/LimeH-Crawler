import urllib2, httplib
from threading import Thread
import time
import requests
from urllib2 import HTTPError
from Sender import Sender

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
                # Request URL from internal /url endpoint
                url = self.request_url()
                # No response or empty string.  Sleep 5s
                if url is None or len(url) == 0:
                    self.sleep(5000)
                # Try to get page
                else:
                    request = self.page_request(url)
                    self.process_result(request, url)
                    self.sleep(800)



	# Input: String URL to grab
	# Behavior: 
	# Output: urllib2 request object
	def page_request(self, url):
            try:
	        #res =  urllib2.urlopen(url)
                return urllib2.urlopen(url)
            # Catch error statuses like 404s
            except HTTPError as e:
                return e


	# Input: urllib2.request object
	# Behavior: Based on result of request, send information to Link Analysis, Text Transformation or Indexing
        # Output: 
	def process_result(self, request, url):
                if request is not None:
                    code = request.getcode()
                    # Success, send to text_transformation
                    if code >= 200 and code < 300:
                        Sender.send_request(Sender.TEXT(), request, url)
                    # Failure, notify indexing and link analysis
                    elif code >= 400 and code < 500:
                        Sender.send_request(Sender.LINK(), request, url)
                        Sender.send_request(Sender.INDEX(), request, url)
                    # Server error
                    elif code >= 500 and code < 600:
                        # TODO store code to check again in XX seconds
                        pass
                    else:
                        #possible redirection or something went terribly wrong
                        pass
		return


        # Input: None
        # Behavior: Request URL from queue
        # Output: 
	def request_url(self):

            try:
                r = requests.post(url = self.URL, data = None)
                response = r.text

                if response is None:
                    print("Failed to get a response")
                    return None
                return response

            except Exception as e:
                print("Exception in Crawler.py " + str(e))
                return None


        # Input: Sleep duration in milliseconds
        # Behavior:
        # Output:
        def sleep(self, duration):
            time.sleep(duration/1000)

