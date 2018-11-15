from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

# True port # is 80
# PORT_ NUMBER = 80

PORT_NUMBER = 8080

class CrawlServer(BaseHTTPRequestHandler):
    
    #Handle POST requests
    def do_POST(self):
        print("Received POST request")
        content_len = int(self.headers['Content-Length'], 0)
        body = self.rfile.read(content_len)
        # Link analysis asking for robots.txt parse
	if self.path == "/robots":
            self.parseRobotstxt(body)
        # Link Analysis giving link to crawl
        elif self.path == "/crawl":
            self.addUrlToQueue(body)
        # Crawler requesting link from queue
        elif self.path == "/url":
            self.sendCrawlerUrl(body)
        else:
            pass
    
    
    def parseRobotstxt(self, body):
        print("/robots\nGot: " + body)
        return
    
    
    def addUrlToQueue(self, body):
        print("/crawl\nGot: " + body)
        return
    
    
    def sendCrawlerUrl(self, body):
        print("/url\nGot: " + body)
        json_string = "https://stackoverflow.com"
        self.respond(json_string)
        return
    
    
    def respond(self, json_string):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(json_string)
        return

    def start(self):
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

