from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

# True port # is 80
# PORT_ NUMBER = 80
PORT_NUMBER = 8080

class CrawlServer(BaseHTTPRequestHandler):
	
	#Handle POST requests
	def do_POST(self):
            # Link analysis asking for robots.txt parse
	    if self.path == "/robots":
                pass
            # Link Analysis giving link to crawl
            elif self.path == "/crawl":
                pass
            # Crawler requesting link from queue
            elif self.path == "/url":
                pass
            else:
                pass
