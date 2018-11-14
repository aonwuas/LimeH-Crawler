from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

# True port # is 80
# PORT_ NUMBER = 80
PORT_NUMBER = 8080

class CrawlServer(BaseHTTPRequestHandler):

	#Handle POST requests
	def do_POST(self):

            content_len = int(self.getheader('content-length',0))
            body = self.rfile.read(content_len)
            # Link analysis asking for robots.txt parse
	    if self.path == "/robots":
                parseRobotstxt(body)
            # Link Analysis giving link to crawl
            elif self.path == "/crawl":
                addUrlToQueue(body)
            # Crawler requesting link from queue
            elif self.path == "/url":
                sendCrawlerUrl(body)
            else:
                pass
    
    
    def parseRobotstxt(self, body):
        return
    
    
    def addUrlToQueue(self, body):
        return
    
    
    def sendCrawlerUrl(self, body):
        return
    
    
    def respond(self, json_string):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(json_string)
        return


#following snippet taken from https://www.acmesystems.it/python_http
try:
    #Create a web server and define the handler to manage the
    #incoming request
    server = HTTPServer(('', PORT_NUMBER), CrawlServer)
    print 'Started httpserver on port ' , PORT_NUMBER

    #Wait forever for incoming htto requests
    server.serve_forever()

except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    server.socket.close()

